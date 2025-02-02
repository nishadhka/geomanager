from .base import *
import os

DEBUG = False

# More secure way to handle SECRET_KEY
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError:
    raise Exception(
        "SECRET_KEY environment variable is not set! Please set it in Replit Secrets."
    )

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# used in dev with Mac OS
GDAL_LIBRARY_PATH = env.str('GDAL_LIBRARY_PATH', None)
GEOS_LIBRARY_PATH = env.str('GEOS_LIBRARY_PATH', None)

try:
    from .local import *
except ImportError:
    pass
