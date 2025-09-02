# settings/dev.py
from .base import *


# Shared application settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG')

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

# Database for local development (PostgreSQL)
# Ensure you have a local PostgreSQL server running with these credentials
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql',
        'NAME'    : os.environ.get('POSTGRES_DB'),
        'USER'    : os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST'    : os.environ.get('POSTGRES_HOST'),
        'PORT'    : os.environ.get('POSTGRES_PORT'),
    }
}
