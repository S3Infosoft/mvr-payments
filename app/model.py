from flask_sqlalchemy import SQLAlchemy
import hashlib

from app.init import app

database = SQLAlchemy(app)

class guest(database.Model):
    __tablename__ = 'guest'
    email = database.Column('email',database.String,primary_key = True)
    name = database.Column('name',database.String)
    phoneno = database.Column('phoneno',database.Integer)
    photoid = database.Column('photoid',database.String)
    reservation = database.relationship("reservation",backref='guest',lazy='dynamic')

    def __init__(self,data):
        self.email = data['email']
        self.name = data['name']
        self.phoneno = data['phoneno']
        self.photoid = data['photoid']

    def update(self,data):
        self.email = data['email']
        self.name = data['name']
        self.phoneno = data['phoneno']
        self.photoid = data['photoid']

    def get_json(self):
        return {
            'email':self.email,
            'name':self.name,
            'phoneno':self.phoneno,
            'photoid':self.photoid
        }

    def __repr__(self):
        return '<Guest %s>' % self.email

class room(database.Model):
    __tablename__ = 'room'
    id     = database.Column('id',database.Integer,primary_key = True)
    res_id = database.Column(database.Integer,database.ForeignKey('reservation.id'))
    type   = database.Column('type',database.String)

    def __init__(self,data):
        self.type = data['type']

class reservation(database.Model):
    __tablename__ = 'reservation'
    id      = database.Column('id',database.Integer,primary_key = True)
    ckin    = database.Column('ckin',database.String)
    ckout   = database.Column('ckout',database.String)
    rdate   = database.Column('rdate',database.String)
    rfrom   = database.Column('rfrom',database.String)
    cmnt    = database.Column('cmnt',database.String)
    
    txn     = database.relationship('payment',backref='reservation',lazy='dynamic')
    guest_id = database.Column(database.String,database.ForeignKey('guest.email'))
    room = database.relationship('room',backref='reservation',lazy='dynamic')

    def __init__(self,data):
        self.rdate = data['rdate']
        self.rfrom = data['rfrom']
        self.ckin  = data['ckin']
        self.ckout = data['ckout']
        self.cmnt = data['cmnt']

    def update(self,data):
        self.rdate = data['rdate']
        self.rfrom = data['rfrom']
        self.ckin  = data['ckin']
        self.ckout = data['ckout']
        self.cmnt = data['cmnt']
                
    def get_json(self):
        user = {
            'id' : self.id,
            'rdate' : self.rdate,
            'rfrom' : self.rfrom,
            'ckin' : self.ckin,
            'ckout' : self.ckout,
            'cmnt' : self.cmnt
        }
        return user

class payment(database.Model):
    __tablename__ = 'payment'
    id       = database.Column('id',database.Integer,primary_key=True)
    txntype  = database.Column('txntype',database.String)
    datetime = database.Column('datetime',database.String)
    payamnt  = database.Column('payamnt',database.Integer)
    paymode  = database.Column('paymode',database.String)
    txnid    = database.Column('txnid',database.String)
    cmnt = database.Column('cmnt',database.String)

    rese_id = database.Column(database.String,database.ForeignKey('reservation.id'))

    def __init__(self,data):
        self.payamnt = data['payamnt']
        self.txntype = data['txntype']
        self.paymode = data['paymode']
        self.txnid   = data['txnid']
        self.datetime = data['datetime']
        self.cmnt = data['cmnt']

    def update(self,data):
        self.payamnt = data['payamnt']
        self.txntype = data['txntype']
        self.paymode = data['paymode']
        self.txnid   = data['txnid']
        self.datetime = data['datetime']
        self.cmnt = data['cmnt']


    def get_json(self):
        data = {
            'payamnt' : self.payamnt,
            'txntype' : self.txntype,
            'paymode' : self.paymode,
            'txnid'   : self.txnid,
            'datetime': self.datetime,
            'cmnt'    : self.cmnt
        }

        return data


class User(database.Model):
    email = database.Column(database.String,primary_key= True)
    password = database.Column(database.String)
    auth = database.Column(database.Boolean, default=True)

    def __init__(self,email,password):
        self.email = email
        self.password = self.__encrypt__(password)

    def __encrypt__(self,password):
        h = hashlib.md5(password.encode())
        return h.hexdigest()

    def verify(self,password):
        return self.password == self.__encrypt__(password)


database.create_all()
