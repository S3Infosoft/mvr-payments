from app.init import app
from app.model import reservation
from flask import json

from app.routes.login import login_api, login_required
from app.routes.guest import guest_api
from app.routes.reservation import reservation_api
from app.auth import jwt_required, fresh_jwt_required

app.register_blueprint(login_api)
app.register_blueprint(guest_api)
app.register_blueprint(reservation_api)

@app.route('/')
@login_required
@jwt_required
def index():
    users = reservation.query.all()
    alluser = []
    for usr in users:
        alluser.append(usr.get_json())
    return json.dumps(alluser)


