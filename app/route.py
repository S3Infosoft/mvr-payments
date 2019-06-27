from flask import request, abort, redirect, Response, url_for, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
import json

import config
from app.init import app
from app.model import reservation, database, payments, User, guest
from app.auth import authentication



login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

@app.route('/dashboard', methods=['POST','GET'])
@login_required
def dashboard():
    return render_template('dashboard.html',User = current_user.email)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        reg_usr = User.query.get(email)
        if reg_usr != None and reg_usr.verify(password):
            print('logged in..')
            login_user(reg_usr)
            return redirect(url_for('dashboard'))
        else:
            err = 'Email and password didnt matched'
            return render_template('login.html',err = err)
    else:
        return render_template('login.html')

@app.route('/signup' , methods = ['GET' , 'POST'])
def signup():
    err = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        new_user = User.query.get(email)

        if new_user == None:
            new_user = User(email,password)
        else:
            err = 'User already present with this email'
            return render_template('signup.html',err = err)
        
        database.session.add(new_user)
        database.session.commit()
        login_user(new_user)

        return redirect(url_for('dashboard'))
    else:
        return render_template('signup.html')

@app.route('/')
@login_required
def index():
    users = reservation.query.all()
    alluser = []
    for usr in users:
        alluser.append(usr.get_json())
    return json.dumps(alluser)


@app.route('/%s/guest/new' % config.VERSION, methods=['POST','GET'])
@login_required
def GuestNew():
    if request.method == 'POST':
        if request.form :
            if guest.query.filter_by(email = request.form['email']).first() is None:
                new_guest = guest(request.form)
                database.session.add(new_guest)
                database.session.commit()

                return render_template('dashboard.html',msg='User %s Registered' % new_guest.name,
                                       GuestView= True,
                                       data=new_guest)
            else:
                err = 'Email is already Registered'
                return render_template('guest_create.html', err = err)
        else:
            render_template('guest_create.html')

    return render_template('guest_create.html')

@app.route('/%s/guest/show' % config.VERSION, methods=['POST','GET'])
@login_required
def GuestShow():
    data = None
    if request.method == 'POST':
        if request.form:
            email = request.form['email']
            g = guest.query.get(email)
            print(g.phoneno)
            if g:
                return render_template('guest_show.html',data=g)

            else:
                return render_template('guest_show.html',data=None , err = 'No any Guest with this Email')
    return render_template('guest_show.html',data=data)

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