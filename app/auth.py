from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

import config

token_serializer = Serializer( config.SECRET_KEY ,
                               expires_in= config.TOKEN_TIME)
                               
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

