from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from init import secret_key

token_serializer = Serializer(secret_key,expires_in=3600)

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