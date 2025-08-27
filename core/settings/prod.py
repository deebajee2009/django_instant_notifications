# settings/prod.py

from .base import *
import os
import dj_database_url

# Production settings
DEBUG = False

# Get allowed hosts from environment variable (comma-separated string)
# e.g., ALLOWED_HOSTS=www.myapp.com,myapp.com
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# --- Production Security Settings ---
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True

# Database configuration from DATABASE_URL environment variable
# e.g., postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)}
