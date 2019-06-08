import requests
import json

class Query:
        def __init__(self,user,pswd):
                self.user = user
                self.pswd = pswd
                self.__url__ = 'http://0.0.0.0:5000'
                self.__ver__ = 'v1'
                self.URL = self.__url__ + '/' + self.__ver__

        def Select(self,Arg):
                if '=' in Arg:
                        col = Arg[:Arg.find('=')]
                        val = Arg[Arg.find('=') + 1:]
                        dmp_url = self.URL + '/Select/' + col + '/' + val
                else:
                        dmp_url = self.__url__

                res = requests.get(dmp_url,auth=(self.user,self.pswd))
                if res.ok:
                        return(res.json())
                else:
                        return res
        
        def Create(self,Args):
                with open(Args) as f:
                        data = json.load(f)
                res = requests.post(self.URL + '/Create',json=data,auth=(self.user,self.pswd))
                if res.ok:
                        return res.json()
                else:
                        return res
        
        def Delete(self,Arg):
                
                res = requests.get(self.URL + '/Delete/' + Arg,auth=(self.user,self.pswd))
                if res.ok:
                        return res.json()
                else:
                        return res

        def Update(self,Arg):

                with open(Arg) as f:
                        data = json.load(f)
                
                print('id : ',data['id'])
                res = requests.post(self.URL + '/Update/' + str(data['id']),json=data,auth=(self.user,self.pswd))
                if res.ok:
                        return res.json()
                else:
                        return res

        def Help(self):
                print("_Help_Here_")
