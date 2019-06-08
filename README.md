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
  - Options are 'all', 'id=<id>'
  - via 'api'
  ```
     Arg = 'all' 
     or 
     Arg = 'id=<id>'

     json_data = Query.Select(Arg)
  ```

  - via 'api_test'

```
    python api_test.py -u=<user_name> -p=<password> select all
    python api_test.py -u=<user_name> -p=<password> select id=<id>
```