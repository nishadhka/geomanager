"""
Django settings for geomanagerweb project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config, Csv

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# Application definition

SECRET_KEY = config("SECRET_KEY",
                    default="django-insecure-change-this-in-production")
DEBUG = False
ALLOWED_HOSTS = [
    '.repl.co', '.replit.dev', '0.0.0.0', 'localhost',
    'geospatial-wagtail-e4drr.replit.app', 'mapviewer'
]
CSRF_TRUSTED_ORIGINS = [
    'https://*.replit.dev', 'https://*.repl.co', 'https://*.replit.dev:8000',
    'http://0.0.0.0:8000', 'http://localhost:3000', 'http://mapviewer:3000',
    'https://geospatial-wagtail-e4drr.replit.app:80'
]

# Mapviewer settings
MAPVIEWER_SERVER_URL = config("MAPVIEWER_SERVER_URL",
                              default="http://localhost:3000")
MAPVIEWER_BASE_PATH = config("MAPVIEWER_BASE_PATH", default="/mapviewer")
MAPVIEWER_ASSET_PREFIX = config("MAPVIEWER_ASSET_PREFIX",
                                default="/mapviewer/static")

# Application definition

INSTALLED_APPS = [
    "home",
    "geomanager",
    "daphne",
    "channels",
    "base",
    "django_deep_translator",
    "adminboundarymanager",
    "django_large_image",
    'django_json_widget',
    'django_nextjs',
    "django_filters",
    "wagtail_color_panel",
    "wagtail_adminsortable",
    "wagtailhumanitarianicons",
    "wagtailiconchooser",
    "django_countries",
    "django_extensions",
    "wagtailfontawesomesvg",
    "wagtail_lazyimages",
    "django_cleanup.apps.CleanupConfig",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "allauth",
    "allauth.account",
    "rest_framework",
    "corsheaders",
    "wagtail_modeladmin",
    "wagtailcache",
    "wagtailmetadata",
    "django.contrib.admin",
    "django.contrib.gis",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "geomanagerweb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "geomanagerweb.wsgi.application"
ASGI_APPLICATION = 'geomanagerweb.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('PGDATABASE'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Django
FORCE_SCRIPT_NAME = config("FORCE_SCRIPT_NAME", default=None)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATICFILES_STORAGE = "base.storage.ManifestStaticFilesStorageNotStrict"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
if FORCE_SCRIPT_NAME:
    STATIC_URL = FORCE_SCRIPT_NAME + STATIC_URL

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

if FORCE_SCRIPT_NAME:
    MEDIA_URL = FORCE_SCRIPT_NAME + MEDIA_URL

# Wagtail settings

WAGTAIL_SITE_NAME = config("WAGTAIL_SITE_NAME", default="GeoManager Web")

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = config('WAGTAILADMIN_BASE_URL', default='')

# Wagtail admin Url path
ADMIN_URL_PATH = config("ADMIN_URL_PATH", default="admin")

NEXTJS_SETTINGS = {
    "nextjs_server_url": config('MAPVIEWER_SERVER_URL', default=None)
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
        'KEY_PREFIX': 'cms_cache',
        'TIMEOUT': 3600,  # one hour (in seconds)
    }
}

# RECAPTCHA Settings
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY', default='')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY', default='')

GEOMANAGER_AUTO_INGEST_RASTER_DATA_DIR = config(
    "GEOMANAGER_AUTO_INGEST_RASTER_DATA_DIR", "")
