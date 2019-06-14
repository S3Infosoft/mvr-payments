from init import app
from model import reservation,database
from auth import authentication, token_serializer
import json, requests

@app.route('/v1/token/<user>')
def get_token(user=None):
    token = token_serializer.dumps({'user':user}).decode('utf-8')
    return token


@app.route('/')
@authentication.login_required
def index():
    users = reservation.query.all()
    alluser = []
    for usr in users:
        alluser.append(user = usr.get_json())
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
    data = requests.get_json()
    user = reservation(data)
    database.session.add(user)
    database.session.commit()
    return 'Data Updated Successfully'

@app.route('/v1/delete/<id>')
@authentication.login_required
def delete(id):
    usr_to_delete = reservation.query.filter_by(id = id).first()
    if usr_to_delete is None:
        return 'no data for id : %s' % id
    
    database.session.delete(usr_to_delete)
    database.session.commit()

    return 'data for id %s deleted successfully' % id

@app.route('/v1/update/<id>',methods=['POST'])
@authentication.login_required
def update(id):
    data = requests.get_json()
    usr_to_update = reservation.query.filter_by(id = id).first()
    usr_to_update(data)

    database.session.commit()

    return 'data update successfully'