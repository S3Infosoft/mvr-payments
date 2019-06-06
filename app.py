#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

db = SQLAlchemy(app)

class Reservations(db.Model):
    ID = db.Column('ID',db.Integer,primary_key = True)
    RDATE = db.Column('RESERVATION DATE', db.String)
    RFROM = db.Column('RESERVATION FROM', db.String(100))
    CKINDATE = db.Column('CHECKIN DATE', db.String)
    CKOUTDATE = db.Column('CHECKOUT DATE',db.String)
    GNAME = db.Column('GUEST NAME', db.String(100))
    GEMAIL = db.Column('GUEST EMAIL', db.String(100))
    GMOBNUM = db.Column('GUEST CONTACT NUMBER', db.Integer)
    BOOKAMNT = db.Column('BOOKING AMOUNT', db.Integer)
    COMAMNT = db.Column('COMMISSION AMOUNT', db.Integer)
    COMTAX = db.Column('COMMISSION TAX', db.Integer)
    TOTCOM = db.Column('TOTAL COMMISSION', db.Integer)
    AMNTREC = db.Column('AMOUNT RECEIVABLE', db.Integer)
    CMNT = db.Column('COMMENTS', db.String(500))

db.create_all()

@app.route('/')
def All():
    users = Reservations.query.all()
    allusers = []

    for user in users:
        new_user = {
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

        allusers.append(new_user)
    
    return json.dumps(allusers)

@app.route('/v1/Select/<method>/<data>')
def Select(method,data):
    if (method == 'id'):
        selected_users = Reservations.query.filter_by(ID = data).all()
    elif (method == 'name'):
        data = str(data)
        data = data.replace('_',' ')
        selected_users = Reservations.query.filter_by(GNAME = data).all()
    else:
        return 'Unknow Method'
    all_selected = []
    for user in selected_users:
        user_data = {
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
        all_selected.append(user_data)

    return json.dumps(all_selected)


if __name__ == '__main__':
    app.run(host='0.0.0.0')