#!/usr/bin/python3
from init import app, db
from Model import Reservations
import json
from flask import request, jsonify, flash, url_for,redirect
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
    elif (method == 'rdate'):
        data = data.replace('_','/')
        selected_users = Reservations.query.filter_by(RDATE = data).all()
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

@app.route('/v1/Create/', methods = ['POST'])
def Create():
    print(request.is_json)
    data = request.get_json()
    print(data)
    user = Reservations(data['Reservation Date'],
                        data['Reservation From'],
                        data['Check in Date'],
                        data['Check Out Date'],
                        data['Guest Name'],
                        data['Guest Email'],
                        data['Guest Contact No.'],
                        data['Booking Amount'],
                        data['Commission Amount'],
                        data['Commission Tax'],
                        data['Total Commission'],
                        data['Amount Recivable'],
                        data['Comment']
           )
    db.session.add(user)
    db.session.commit()

    flash('data added successfully')
    
    return redirect(url_for('All'))

@app.route('/v1/Delete/<uid>')
def Delete(uid):
    user_to_delete = Reservations.query.filter_by(ID = uid).all()[0]
    db.session.delete(user_to_delete)
    db.session.commit()
    flash('data for ID %s Deleted Successfully'%uid)
    return redirect(url_for('All'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')