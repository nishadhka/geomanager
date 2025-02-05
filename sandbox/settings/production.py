from .base import *
import os

DEBUG = False

# More secure way to handle SECRET_KEY
#SECRET_KEY = os.environ.get('SECRET_KEY')
# In production.py
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-this-in-production")

if not SECRET_KEY:
    raise Exception(
        "SECRET_KEY environment variable is not set or is empty! Please set it in your environment."
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
