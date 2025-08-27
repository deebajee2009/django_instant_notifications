# settings/dev.py

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Use a simple, insecure key for local development
SECRET_KEY = 'django-insecure-4k!q!&+__vl790!1t45+ziy8nd6$6@ra1b16s9z-cxlh6^@=u!'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database for local development (PostgreSQL)
# Ensure you have a local PostgreSQL server running with these credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_project_db',
        'USER': 'my_project_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
