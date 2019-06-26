import os

__secret_key__ = os.urandom(36)
__token_time__ = 5 * 60