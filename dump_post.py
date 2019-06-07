import requests

user_data = {
            'Reservation Date' : '25/05/1998',
            'Reservation From' : 'Google',
            'Check in Date': '26/06/2016',
            'Check Out Date' : '25/07/2019',
            'Guest Name' : 'Another Dumy User',
            'Guest Email' : 'ADU123@gmail.com',
            'Guest Contact No.' : 96241256200,
            'Booking Amount' : 600,
            'Commission Amount' : 250,
            'Commission Tax': 985,
            'Total Commission' : 6523,
            'Amount Recivable' : 200,
            'Comment' : 'Testing Dumy User to Add via Request',
        }
res = requests.post('http://0.0.0.0:5000/v1/Create',json=user_data)
if res.ok:
    print(res.json())