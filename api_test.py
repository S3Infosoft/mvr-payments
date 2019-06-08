import requests
import sys
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


options = ['select','create','delete','update','addadmin']

if __name__ == '__main__':

        user       = None
        password   = None
        cmd_found  = False
        option     = None
        Arg        = None
        for i in sys.argv[1:]:
                if "-u=" in i:
                        user = i[3:]

                elif "-p=" in i:
                        password = i[3:]

                elif i in options and not cmd_found:
                        option = i
                        cmd_found = True
                
                else:
                        Arg = i

        q = Query(user,password)

        if option == 'select':
                print(q.Select(Arg))
        
        elif option == 'update':
                print(q.Update(Arg))

        elif option == 'create':
                print(q.Create(Arg))

        elif option == 'delete':
                print(q.Delete(Arg))
        else:
                print("___Help__Here___")

