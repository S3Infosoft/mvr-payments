#!/usr/bin/python3

from sqlalchemy import Table, create_engine, MetaData, Column, String, Integer, Date, UniqueConstraint
engine = create_engine("sqlite:///../database.db", echo = True)
meta = MetaData()

RESERVATION = Table(
    'RESERVATION', meta,
    Column('ID',Integer,primary_key = True),
    Column('RESERVATION DATE',String),
    Column('RESERVATION FROM',String),
    Column('CHECKIN DATE', Date),
    Column('CHECKOUT DATE',Date),
    Column('GUEST NAME', String),
    Column('GUEST EMAIL', String),
    Column('GUEST CONTACT NO', Integer),
    Column('BOOKING AMOUNT', Integer),
    Column('COMMISSION AMOUNT',Integer),
    Column('COMMISSION TAX', Integer),
    Column('TOTAL COMMISSION', Integer),
    Column('AMOUNT RECEIVABLE', Integer),
    Column('COMMENTS',String)
)


PAYMENT = Table(
    'PAYMENT', meta,
    Column('ID',Integer, primary_key = True),
    Column('PAYMENT AMOUNT',Integer),
    Column('PAYMENT METHOD', String),
    Column('TXN ID',Integer),
    UniqueConstraint('TXN ID'),
)


#Create Table
meta.create_all(engine)