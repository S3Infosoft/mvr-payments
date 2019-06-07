from flask_httpauth import HTTPBasicAuth
from Model import AuthUser
auth = HTTPBasicAuth()

@auth.verify_password
def VerifyPassword(username,password):
    user = AuthUser.query.filter_by(user = username).first()
    if not user or not user.verify(password):
        return False
    return True