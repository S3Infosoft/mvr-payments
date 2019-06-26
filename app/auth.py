from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from config import __secret_key__, __token_time__

token_serializer = Serializer(__secret_key__,expires_in=__token_time__)
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

