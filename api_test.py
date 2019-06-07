import requests
import sys
import json

__url__ = 'http://0.0.0.0:5000'
__ver__ = 'v1'

HELP_MSG = """
Create <json-file>       :       To Create Database
Update <id> <json-file>  :       To Update Database
Select id <id>           :       List User of Selected ID
Delete <id>              :       Delete User of Specified ID
"""

if __name__ == '__main__':

        if len(sys.argv) == 1:
                print(HELP_MSG)
        
        elif sys.argv[1] == 'Select':
                if sys.argv[2] == 'all':
                        res = requests.get(__url__)
                        if res.ok:
                                print(res.json())
                elif len(sys.argv) == 4:
                        url = __url__ + '/' + __ver__ + '/Select/' + sys.argv[2] + '/' + sys.argv[3]
                        res = requests.get(url)
                        if res.ok:
                                print(res.json())
                else:
                        print("Either use 'Select all' or 'Select id <id>'")

        elif sys.argv[1] == 'Create' and len(sys.argv) == 3:
                data_file = sys.argv[2]
                with open(data_file) as f:
                        data = json.load(f)
                url = __url__ + '/' + __ver__ + '/Create'
                res = requests.post(url,json=data)
                
                if res.ok:
                        print("Data Created")

        elif sys.argv[1] == 'Delete' and len(sys.argv) == 3:
                url = __url__ + '/' + __ver__ + '/Delete/' + sys.argv[2]
                res = requests.get(url)

                if res.ok:
                        print("Data for %s Deleted"%sys.argv[2])

        elif sys.argv[1] == 'Update' and len(sys.argv) == 4:
                data_file = sys.argv[3]
                with open(data_file) as f:
                        data = json.load(f)
                
                url = __url__ + '/' + __ver__ + '/Update/' + sys.argv[2]

                res = requests.post(url,json=data)
                if res.ok:
                        print("Data Updated")
        
        elif sys.argv[1] == 'AuthUser' and len(sys.argv) == 4:
                data_file = sys.argv[3]
                with open(data_file) as f:
                        data = json.load(f)
                url = __url__ + '/' + __ver__ + "/auth/" + sys.argv[2]

                res = requests.post(url,json=data)
                if res.ok:
                        print("AuthUser Created")
        else:
                print(HELP_MSG)
