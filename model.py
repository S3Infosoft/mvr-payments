from init import app
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy(app)

class reservation(database.Model):
    id      = database.Column('id',database.Integer,primary_key = True)
    rdate   = database.Column('rdate',database.String)
    rfrom   = database.Column('rfrom',database.String)
    ckin    = database.Column('ckin',database.String)
    ckout   = database.Column('ckout',database.String)
    gname   = database.Column('gname',database.String)
    gemail  = database.Column('gemail',database.String)
    gcontno = database.Column('gcontno',database.Integer)
    amntbook= database.Column('amntbook',database.Integer)
    amntcom = database.Column('amntcom',database.Integer)
    taxcom  = database.Column('taxcom',database.Integer)
    totcom  = database.Column('totcom',database.Integer)
    amntrec = database.Column('amntrec',database.Integer)
    cmnt =    database.Column('cmnt',database.String)

    def __init__(self,data):
        self.rdate = data['rdate']
        self.rfrom = data['rfrom']
        self.ckin  = data['ckin']
        self.ckout = data['ckout']
        self.gname = data['gname']
        self.gcontno = data['gcontno']
        self.gemail = data['gemail']
        self.amntbook = data['amntbook']
        self.amntcom = data['amntcom']
        self.taxcom = data['taxcom']
        self.totcom = data['totcom']
        self.amntrec = data['amntrec']
        self.cmnt = data['cmnt']

    def get_json(self):
        user = {
            'id' : self.id,
            'rdate' : self.rdate,
            'rfrom' : self.rfrom,
            'ckin' : self.ckin,
            'ckout' : self.ckout,
            'gname' : self.gname,
            'gemail' : self.gemail,
            'gcontno' : self.gcontno,
            'bkamnt' : self.bkamnt,
            'comamnt' : self.comamnt,
            'comtax' : self.comtax,
            'comtot' : self.comtot,
            'amntrec' : self.amntrec,
            'cmnt' : self.cmnt
        }
        return user

class payments(database.Model):
    payamnt = database.Column('payamnt',database.Integer)
    paymeth = database.Column('paymeth',database.String)
    txnid   = database.Column('txnid',database.String)
    resid   = database.Column('resid',database.Integer,primary_key=True)
    datetime = database.Column('datetime',database.String)
    creator  = database.Column('creator',database.String)
    cmnt = database.Column('cmnt',database.String)

    def __init__(self,data):
        self.payamnt = data['payamnt']
        self.paymeth = data['paymeth']
        self.txnid   = data['txnid']
        self.resid   = data['resid']
        self.datetime = data['datetime']
        self.creator = data['creator']
        self.cmnt = data['cmnt']

    def get_json(self):
        data = {
            'payamnt' : self.payamnt,
            'paymeth' : self.paymeth,
            'txnid'   : self.txnid,
            'resid'   : self.resid,
            'datetime': self.datetime,
            'creator' : self.creator,
            'cmnt'    : self.cmnt
        }

        return data
    
database.create_all()
