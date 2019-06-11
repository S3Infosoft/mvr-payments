#!/usr/bin/python3
from init import app, db
from Model import Reservations,AuthUser
from auth import auth
import json
from flask import request, jsonify, flash, url_for,redirect, abort

@app.route('/v1/auth/<admin_pass>',methods = ['POST'])
def NewUser(admin_pass):
    admin = AuthUser.query.filter_by(user = 'admin').first()
    if not admin.verify(admin_pass):
        abort(403)

    data = request.get_json()
    try:
        if AuthUser.query.filter_by(user = data['userid']).first() is None:
            abort(406)
        
        user = AuthUser(user = data['userid'])
        user.__hash__(data['password'])
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('All'))

    except KeyError as e:
        abort(400)

@app.route('/',methods=['GET','POST'])
@auth.login_required
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
@auth.login_required
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
@auth.login_required
def Create():
    data = request.get_json()
    try:
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

        return 'Data Updated Successfully'

    except KeyError as e:
        return 'Data Error : one or more entries are missing\nCode : %s'%str(e)


@app.route('/v1/Delete/<uid>')
@auth.login_required
def Delete(uid):
    user_to_delete = Reservations.query.filter_by(ID = uid).all()[0]
    db.session.delete(user_to_delete)
    db.session.commit()
    flash('data for ID %s Deleted Successfully'%uid)
    return redirect(url_for('All'))

@app.route('/v1/Update/<uid>',methods=['POST'])
@auth.login_required
def Update(uid):
    data = request.get_json()
    user_to_update = Reservations.query.filter_by(ID = uid).first()
    try:
        user_to_update.RDATE = data['Reservation Date']
    except KeyError:
        pass

    try:
        user_to_update.RFROM = data['Reservation From']
    except KeyError:
        pass

    try:
        user_to_update.CKINDATE = data['Check in Date']
    except KeyError:
        pass

    try:
        user_to_update.CKOUTDATE = data['Check Out Date']
    except KeyError:
        pass

    try:
        user_to_update.GNAME = data['Guest Name']
    except KeyError:
        pass

    try:
        user_to_update.GEMAIL = data['Guest Email']
    except KeyError:
        pass

    try:
        user_to_update.GMOBNUM = data['Guest Contact No.']
    except KeyError:
        pass

    try:
        user_to_update.BOOKAMNT = data['Guest Email']
    except KeyError:
        pass

    try:
        user_to_update.COMAMNT = data['Commission Amount']
    except KeyError:
        pass

    try:
        user_to_update.COMTAX = data['Commission Tax']
    except KeyError:
        pass

    try:
        user_to_update.TOTCOM = data['Total Commission']
    except KeyError:
        pass

    try:
        user_to_update.AMNTREC = data['Amount Recivable']
    except KeyError:
        pass

    try:
        user_to_update.CMNT = data['Comment']
    except KeyError:
        pass
    
    db.session.commit()

    flash("Data Updated Successfully")

    return redirect(url_for('All'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')