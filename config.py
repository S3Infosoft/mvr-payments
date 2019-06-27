import os

VERSION = 'v1'
SECRET_KEY = os.urandom(36)
TOKEN_TIME = 5 * 60


__roots__ = '../'

TEMPLATES = __roots__ + 'templates'
STATIC = __roots__ + 'static'

DATATBASE = __roots__ + 'database/database.db'