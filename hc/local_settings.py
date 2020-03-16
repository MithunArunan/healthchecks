import os
import warnings

def envbool(s, default):
    v = os.getenv(s, default=default)
    if v not in ("", "True", "False"):
        msg = "Unexpected value %s=%s, use 'True' or 'False'" % (s, v)
        raise Exception(msg)
    return v == "True"

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

SITE_ROOT = os.environ['SITE_ROOT']

EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_PORT = int(os.environ["EMAIL_PORT"])
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS = envbool("EMAIL_USE_TLS", "True")
EMAIL_USE_VERIFICATION = envbool("EMAIL_USE_VERIFICATION", "True")

DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]