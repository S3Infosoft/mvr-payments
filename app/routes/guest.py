from flask import Blueprint, json
from flask import request, render_template

import config
from app.model import database, guest
from app.routes.login import login_required
from app.auth import fresh_jwt_required

guest_api = Blueprint('guest_api',__name__)


# ----------------------------------------------------------------

@guest_api.route('/%s/guest/select/<email>' % config.VERSION)
#@fresh_jwt_required
def guest_select(email):
    sel_guest = guest.query.get(email)
    if sel_guest is None:
        return 404
    return json.dumps(sel_guest.get_json())

@guest_api.route('/%s/guest/create' % config.VERSION , methods = ['POST'])
#@fresh_jwt_required
def guest_create():
    data = request.get_json()
    if guest.query.get(data['email']) is None:
        new_guest = guest(data)
        database.session.add(new_guest)
        database.session.commit()
        return json.dumps(data)
    else:
        return 404

@guest_api.route('/%s/guest/update/<email>' % config.VERSION ,methods = ['POST'])
#@fresh_jwt_required
def guest_update(email):
    data = request.get_json()
    sel_guest = guest.query.get(email)
    if sel_guest is None:
        return 404
    
    sel_guest.update(data)
    database.session.commit()
    return json.dumps(data)