#!/usr/bin/env python3

import requests
import sys

__url__ = 'http://0.0.0.0:5000'

class api:
    def __init__(self,user):
        self.token = requests.get(__url__ + '/v1/token/' + user).text

    def __get__(self,url):
        r = requests.get(url,headers={'Authorization':'Bearer %s' % self.token})
        return r,r.text
        
    def select(self,id):
        if id == 'all':
            return self.__get__(__url__ + '/')
        return self.__get__(__url__ + '/v1/select/' + str(id))

if __name__ == '__main__':
    option = sys.argv[1]
    arg = sys.argv[2]

    a = api('admin')
    print(a.token)
    print(a.select(arg))
