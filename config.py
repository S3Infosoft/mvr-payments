import os

__version__ = 'v1'
__secret_key__ = os.urandom(36)
__token_time__ = 5 * 60