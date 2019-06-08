# mvr-payments
MVR Payments Module

## To Build 
- docker build -t mvr-payment:latest .

## To Run
- docker run -d -p 5000:5000 mvr-payment:latest

## Api Test
api contain a python class 'Query' with initial arguments 'username' and 'password' of registered user for authentication.
class 'Query' contain members 'Select', 'Update', 'Create', 'Delete'

### To Select
To Select or List Selected or all users of the database 
  - Options are 'all', 'id=<id>'

#### via 'api'
  ```
     Arg = 'all' 
     or 
     Arg = 'id=<id>'

     json_data = Query.Select(Arg)
  ```

#### via 'api_test'

```
    python api_test.py -u=<user_name> -p=<password> select all
    python api_test.py -u=<user_name> -p=<password> select id=<id>
```

### To Create
To add new user to the database
The Json Data File that going to use to create new user database should contain all the entries except 'id' that will automatically assigned to the user
#### via 'api'

```
    Query.Create(<json-file-address>)
```

#### via 'api_test'

```
    python api_test.py -u=<user_name> -p=<password> create <json-file-addr>
```

### To Delete
To delete the data of existing user

#### via 'api'
```
    Query.Delete(<id>)
```

#### via 'api_test'

```
    python api_test.py -u=<user_name> -p=<password> delete <id>
```

### To Update
to update the data of existing user
json file that is going to Update the database should atleast contain the 'id' thats going to be updated
and may contain all the entries
#### via 'api'
```
    Query.Update(<json-file-address>)
```

#### via 'api_test'
```
    python api_test.py -u=<user_name> -p=<password> update <json-file-address>
```

