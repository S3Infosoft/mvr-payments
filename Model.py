from init import db

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

    def __init__(self,RDATE, RFROM, CKINDATE,CKOUTDATE, GNAME, GEMAIL, GMOBNUM, BOOKAMNT, COMAMNT, COMTAX, TOTCOM, AMNTREC, CMNT):
        self.RDATE = RDATE
        self.RFROM = RFROM
        self.CKINDATE = CKINDATE
        self.CKOUTDATE = CKOUTDATE
        self.GNAME = GNAME
        self.GEMAIL = GEMAIL
        self.GMOBNUM = GMOBNUM
        self.BOOKAMNT = BOOKAMNT
        self.COMAMNT = COMAMNT
        self.COMTAX = COMTAX
        self.TOTCOM = TOTCOM
        self.AMNTREC = AMNTREC
        self.CMNT = CMNT

db.create_all()