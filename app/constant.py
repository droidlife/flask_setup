import os
SERVER = os.environ['SERVER']

if SERVER == 'testing':
    DB_CONNECTION_URL = 'sqlite:////tmp/test.db'
else:
    DB_USER_NAME = os.environ['DB_USER_NAME']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_NAME = os.environ['DB_NAME']
    DB_CONNECTION_URL = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(DB_USER_NAME, DB_PASSWORD, DB_HOST, DB_NAME)
