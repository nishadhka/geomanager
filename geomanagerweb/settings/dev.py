from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-development-key')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,0.0.0.0').split(',')

# Database configuration for Replit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('CMS_DB_NAME', 'geomanager'),
        'USER': os.getenv('CMS_DB_USER', 'geomanager'),
        'PASSWORD': os.getenv('CMS_DB_PASSWORD', 'geomanager'),
        'HOST': os.getenv('CMS_DB_HOST', 'localhost'),
        'PORT': os.getenv('CMS_DB_PORT', '5432'),
    }
}

# Static files configuration for Replit
STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('STATIC_ROOT', '/home/app/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.getenv('MEDIA_ROOT', '/home/app/media')

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CORS_ALLOW_ALL_ORIGINS = True

INSTALLED_APPS += [
    'wagtail.contrib.styleguide'
]

# MapViewer configuration
MAPVIEWER_BASE_PATH = os.getenv('MAPVIEWER_BASE_PATH', '/mapviewer')
MAPVIEWER_ASSET_PREFIX = os.getenv('MAPVIEWER_ASSET_PREFIX', '/mapviewer/static')
