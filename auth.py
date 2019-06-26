from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from init import secret_key

__token_time__ = 3600

token_serializer = Serializer(secret_key,expires_in=__token_time__)

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

