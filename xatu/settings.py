import os


VERSION = '0.1.0'
TITLE = 'Xatu'
DEBUG = os.getenv('DEBUG') == 'true'
ENVIRONMENT = os.getenv('ENVIRONMENT')
IS_PRODUCTION = ENVIRONMENT == 'production'

ALLOWED_ORIGINS = '*'

ARANGO_URL = f'http://{os.getenv("ARANGO_HOST")}:{os.getenv("ARANGO_PORT")}'
ARANGO_DB_NAME = os.getenv('ARANGO_DB_NAME')
ARANGO_PASSWORD = os.getenv('ARANGO_PASSWORD')
