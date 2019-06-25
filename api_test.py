#!/usr/bin/env python3

from auth import get_token
import requests
import sys
import os
import json
__url__ = 'http://0.0.0.0:5000/'
__version__ = 'v1'

queries = ['select','create','delete','update']

class api:
    def __init__(self,token):
        self.head = {'Authorization': 'Bearer ' + token}

    def get(self,url):
        res = requests.get(url,headers=self.head)
        return res, res.text

    def post(self,url,js):
        res = requests.post(url,headers=self.head,json=js)
        return res, res.text

    def select(self,id):
        if id == 'all':
            url = __url__ + '/'
        else:
            url = __url__ + __version__ + '/select/' + str(id)
        return self.get(url)

    def create(self,js):
        if os.path.isfile(js):
            with open(js,'r') as js_file:
                data = json.load(js_file)
        else:
            data = js

        url = __url__ + __version__ + '/create/'
        print(url)
        return self.post(url,data)

    def delete(self,id):
        url = __url__ + __version__ + '/delete/' + id
        return self.get(url)

    def update(self,id_json):
        url = __url__ + __version__ + '/update/' + id_json[0]

        if os.path.isfile(id_json[1]):
            with open(id_json[1],'r') as js_data:
                data = json.load(js_data)
        else:
            data = id_json[1]

        return self.post(url,data)



if __name__ == '__main__':
    if sys.argv[1] in queries:
        query = sys.argv[1]

    arg = sys.argv[2:]

    token = get_token('admin')
    a = api(token)

    if query == 'select':
        print(a.select(arg[0]))

    elif query == 'create':
        print(a.create(arg[0]))

    elif query == 'delete':
        print(a.delete(arg[0]))
    
    elif query == 'update':
        print(a.update(arg))
