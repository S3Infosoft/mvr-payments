#!/usr/bin/python3
from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Reservations(db.Model):
    ID = db.Column('ID', db.Integer, primary_key = True)
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

db.init_app(app)
db.create_all()
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

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0')