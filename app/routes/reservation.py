from flask import (
    Blueprint,
    request,
    json,
)

from app.model import database, guest, reservation
from app.auth import fresh_jwt_required
from app.routes.login import login_required

import config

reservation_api = Blueprint('reservation_api',__name__)

@reservation_api.route('/%s/reservation/create/<email>' % config.VERSION, methods = ['POST'])
@fresh_jwt_required
def reservation_create(email):
    data = request.get_json()
    sel_guest = guest.query.get(email)

    if sel_guest is None: return 404
    
    new_res = reservation(data)
    sel_guest.reservation.append(new_res)
    database.session.add(new_res)
    database.session.commit()

    return 200

@reservation_api.route('/%s/reservation/select/<id>' % config.VERSION, methods = ['GET'])
@fresh_jwt_required
def reservation_select(id):
    if id == 'all':
        res = reservation.query.all()
        all_res = []
        for r in res:
            all_res.append(r.get_json())

        return json.dumps(all_res)
    else:
        res = reservation.query.get(id)
        
        if res is None: return 404
        
        return res.get_json()

@reservation_api.route('/%s/reservation/guest/<email>' % config.VERSION, methods = ['GET'])
@fresh_jwt_required
def reservation_guest(email):
    sel_guest = guest.query.get(email)
    
    if sel_guest is None: return 404

    guest_res_all = []
    for r in sel_guest.reservation:
        guest_res_all.append(r.get_json())
    
    return json.dumps(guest_res_all)

@reservation_api.route('/%s/reservation/update/<id>' % config.VERSION, methods = ['POST'])
@fresh_jwt_required
def reservation_update(id):
    sel_res = reservation.query.get(id)
    
    if sel_res is None: return 404
    
    data = request.get_json()
    sel_res.update(data)
    database.commit()

    return 202

@reservation_api.route('/%s/reservation/delete/<id>' % config.VERSION, methods = ['POST'])
@fresh_jwt_required
def reservation_delete(id):
    sel_res = reservation.query.get(id)
    
    if sel_res is None: return 404
    
    database.session.delete(sel_res)
    database.commit()
    return 202