from flask import (
    Blueprint,
    request,
    render_template, redirect, url_for
)

from flask_login import (
    LoginManager,
    login_required,
    current_user,
    login_user, logout_user
)

from app.init import app
from app.model import database, User

login_api = Blueprint('login_api',__name__)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_api.route('/dashboard', methods=['POST','GET'])
@login_required
def dashboard():
    return render_template('dashboard.html',
                            User = current_user.email)



@login_api.route('login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email    = request.form['email']
        password = request.form['password']

        reg_usr  = User.query.get(email)

        if reg_usr is not None and reg_usr.verify(password):
            login_user(reg_usr)
            print('logged in %s' % current_user.email)

            return redirect(url_for('dashboard'))
        
        else:
            if reg_usr is None:
                err = 'No User with this email address'
            else:
                err = 'Password didnt matched'
            
            return render_template('login.html',err = err)
    else:

        return render_template('login.html')


@login_api.route('/signup', methods=['GET','POST'])
def signup():
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




@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)