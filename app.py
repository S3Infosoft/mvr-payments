#!/usr/bin/python3
from flask import request
import json
from Models import Reservations, app, db

@app.route('/')
def Fetch():
    USERS = Reservations.query.all()
    ALL = []
    for user in USERS:
        new = {
            'id' : user.ID,
            'Reservation Date' : user.RDATE,
            'Reservation From' : user.RFROM,
            'Check in Date': user.CKINDATE,
            'Check Out Date' : user.CKOUTDATE,
            'Guest Name' : user.GNAME,
            'Guest Email' : user.GEMAIL,
            'Guest Contact No.' : user.GMOBNUM,
            'Booking Amount' : user.BOOKAMNT,
            'Commission Amount' : user.COMAMNT,
            'Commission Tax': user.COMTAX,
            'Total Commission' : user.TOTCOM,
            'Amount Recivable' : user.AMNTREC,
            'Comment' : user.CMNT
        }
        ALL.append(new)
    
    return json.dumps(ALL), 200

@app.route('/Create', methods=['POST'])
def add():
    data = request.get_json()
    name = data['']

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0')