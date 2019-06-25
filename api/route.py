import json
from flask import request
from api.init import app
from api.config import __secret_key__
from api.model import database, reservation, payments
from api.auth import authentication, token_serializer

@app.route('/')
@authentication.login_required
def index():
    users = reservation.query.all()
    alluser = []
    for usr in users:
        alluser.append(usr.get_json())
    return json.dumps(alluser)


@app.route('/v1/select/<id>')
@authentication.login_required
def select(id):
    sel_usr = reservation.query.filter_by(id = id).first()
    if sel_usr is None:
        return 'no user with id = %s' % id
    return json.dumps(sel_usr.get_json())


@app.route('/v1/create/', methods = ['POST'])
@authentication.login_required
def create():
    data = request.get_json()
    user = reservation(data)
    database.session.add(user)
    database.session.commit()
    return str('Data Updated Successfully')

@app.route('/v1/delete/<id>')
@authentication.login_required
def delete(id):
    usr_to_delete = reservation.query.filter_by(id = id).first()
    if usr_to_delete == None:
        return 'no data for id %s' % id
    else:
        database.session.delete(usr_to_delete)
        database.session.commit()

        return 'data for id %s deleted successfully' % id

@app.route('/v1/update/<id>',methods=['POST'])
@authentication.login_required
def update(id):
    data = request.get_json()
    usr = reservation.query.filter_by(id = id).first()
    if usr == None:
        return 'not existing user for id : %s' % id
    usr.update(data)
    database.session.commit()

    return 'data update successfully'