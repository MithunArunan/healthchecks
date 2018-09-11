import os

DATABASES = {
    'default': {
        'ENGINE':   os.environ['DB_ENGINE'],
        'NAME':     os.environ['DB_NAME'],
        'USER':     os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ.get('DB_HOST'),
        'TEST': {'CHARSET': 'UTF8'}
    }
}

SLACK_CLIENT_ID = os.environ['SLACK_CLIENT_ID']
SLACK_CLIENT_SECRET = os.environ['SLACK_CLIENT_SECRET']
