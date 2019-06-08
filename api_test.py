import sys
from api import Query

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

