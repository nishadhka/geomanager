import secrets
from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

WAGTAIL_ENABLE_UPDATE_CHECK = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.token_urlsafe(64)
#SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
#ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

ALLOWED_HOSTS = [
    '.repl.co', '.replit.dev', '0.0.0.0', 'localhost',
    'geospatial-wagtail-e4drr.replit.app', 'mapviewer'
]

DEBUG = env('DEBUG', False)

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
