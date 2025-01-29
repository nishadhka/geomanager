from .base import *
from environ import Env

env = Env()

DEBUG = False

# Security settings
SECRET_KEY = env.str('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Database
DATABASES = {
    'default': env.db()
}

# SSL/HTTPS settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env.str('EMAIL_HOST', 'localhost')
EMAIL_PORT = env.int('EMAIL_PORT', 25)
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', False)

try:
    from .local import *
except ImportError:
    pass
