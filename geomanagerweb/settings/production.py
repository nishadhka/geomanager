import os
import secrets
from decouple import config
from .base import *

try:
    from .local import *
except ImportError:
    pass

WAGTAIL_ENABLE_UPDATE_CHECK = False

SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(64))

ALLOWED_HOSTS = [
    '*', 'https://*.replit.app', '.repl.co', '.replit.dev', '0.0.0.0'
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.repl.co', 'https://*.replit.dev', 'https://*.replit.app'
] + config('CSRF_TRUSTED_ORIGINS', default='').split(',')

DEBUG = False
SECURE_CROSS_ORIGIN_OPENER_POLICY = config(
    "SECURE_CROSS_ORIGIN_OPENER_POLICY", default=None)

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='').split(',')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

WAGTAIL_CACHE = False
