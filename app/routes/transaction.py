from flask import (
    Blueprint,
    request,
    json
)

import config
from app.auth import fresh_jwt_required
from app.model import database, reservation, payment
transaction_api = Blueprint('transaction_api',__name__)

@transaction_api.route('/%s/transaction/create' % config.VERSION, methods=['POST'])
#@fresh_jwt_required
def transaction_create():
    data = request.get_json()
    rs_id = data['rs_id']
    res = reservation.query.get(rs_id)
    
    if res is None: return 404

    new_tran = payment(data)
    res.txn.append(new_tran)
    database.session.add(new_tran)
    database.session.commit()

    return json.dumps(new_tran.get_json())

@transaction_api.route('/%s/transaction/select/<id>' % config.VERSION, methods = ['GET'])
#@fresh_jwt_required
def transaction_select(id):
    txns = payment.query.get(id)

    if txns is None: return 404
    
    return txns.get_json()

@transaction_api.route('/%s/transaction/reservation/<id>' % config.VERSION, methods = ['GET'])
#@fresh_jwt_required
def transaction_select_reservation(id):
    res = reservation.query.get(id)

    if res is None: return 200
    
    txns = []
    
    for txn in res.txn:
        txns.append(txn.get_json())

    return json.dumps(txns)

@transaction_api.route('/%s/transaction/update/<id>' % config.VERSION, methods = ['POST'])
#@fresh_jwt_required
def transaction_update(id):
    txns = payment.query.get(id)

    if txns is None: return 404

    data = request.get_json()
    txns.update(data)
    database.session.commit()

    return 202