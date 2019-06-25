# mvr-payments
MVR Payments Module

## To Build 
``` docker build -t mvr-payment:latest . ```

## To Run
``` docker run --rm -p 5000:5000 -d --name s3infosoft mvr-payment:latest ```

## Token based authentication
to get token which is valid for 1hr

``` docker exec -it s3infosoft python gettoken.py ```

## Api Test
 to test apis a python script api_test.py is used
 
 ### to select 
 ``` docker exec -it s3infosoft python api_test.py select <id>/'all' ```
 
 ### to create
 ``` docker exec -it s3infosoft python api_test.py create sample/NewUser.json ```

 ### to update
 ``` docker exec -it s3infosoft python api_test.py update <id> sample/Update.json ```

 ### to delete
 ``` docker exec -it s3infosoft python api_test.py delete <id>```

### Links

- main : http://0.0.0.0:5000/
- Select : http://0.0.0.0:5000/v1/select/<id>
- Create : http://0.0.0.0:5000/v1/create/
- Delete : http://0.0.0.0:5000/v1/delete/<id>
- Update : http://0.0.0.0:5000/v1/update/<id>

