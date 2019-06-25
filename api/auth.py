from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from config import __token_time__
from api.init import secret_key,app
import api.model
import hashlib

<<<<<<< HEAD:api/auth.py
<<<<<<< HEAD:api/auth.py
from api.config import __secret_key__, __token_time__

token_serializer = Serializer(__secret_key__,expires_in=__token_time__)

=======

token_serializer = Serializer(secret_key,expires_in=__token_time__)
>>>>>>> a3f00e02aeeac71ff07bf4a53c2ecb857110c7e6:api/auth.py
=======

token_serializer = Serializer(secret_key,expires_in=__token_time__)
>>>>>>> a3f00e02aeeac71ff07bf4a53c2ecb857110c7e6:api/auth.py
authentication = HTTPTokenAuth('Bearer')

@authentication.verify_token
def verify_token(token=None):
    try:
        data = token_serializer.loads(token)
    except:
        return False

    if 'user' in data:
        return True

    return False


def get_token(user=None):
    token = token_serializer.dumps({'user':user}).decode('utf-8')
    return token


def encrypt(passwd):
    obj = hashlib.sha224(passwd.encode())
    return obj.hexdigest()

def verify(pass_hash,passwd):
    return pass_hash == encrypt(passwd)


