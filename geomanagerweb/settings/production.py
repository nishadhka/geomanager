import os
import secrets
from .base import *

try:
    from .local import *
except ImportError:
    pass

WAGTAIL_ENABLE_UPDATE_CHECK = False

SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(64))

ALLOWED_HOSTS = ['*', '.repl.co', '.replit.dev', '0.0.0.0']

CSRF_TRUSTED_ORIGINS = [
    'https://*.repl.co',
    'https://*.replit.dev',
    'https://*.replit.app'
]

DEBUG = False

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', cast=None, default=[])
SECURE_CROSS_ORIGIN_OPENER_POLICY = env.str(
    "SECURE_CROSS_ORIGIN_OPENER_POLICY", None)

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', cast=None, default=[])

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

WAGTAIL_CACHE = False
