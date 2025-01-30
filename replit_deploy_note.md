# Geomanager Installation Documentation

## Installation Steps and Changes Made

### 1. Fixed GDAL Installation Using Wheels:
```sh
pip install --find-links https://girder.github.io/large_image_wheels GDAL
```
 Distutils Error
### 2. Installed Gunicorn Server:
```sh
pip install "gunicorn==20.0.4"
```

### 3. Installed Project Requirements:
```sh
pip install -r sandbox/requirements.txt
```

### 4. Installed Geomanager Package:
```sh
pip install geomanager
```

### 5. First Attempt at Collecting Static Files Failed.

### 6. Second Attempt with Correct Path:
```sh
python sandbox/manage.py collectstatic --noinput --clear
```

### 7. Fixed Missing Dependency by Installing `django_deep_translator`:
```sh
pip install django_deep_translator
```

### 8. Final `collectstatic` Command Resolved Static Files:
```sh
python sandbox/manage.py collectstatic --noinput --clear
```

Change in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['PGDATABASE'],
        'USER': os.environ['PGUSER'],
        'PASSWORD': os.environ['PGPASSWORD'],
    }
}
Re-run migrations:

Re-run migrations:
python sandbox/manage.py migrate
3. Auto-created Primary Key Warning
Warning Message: Auto-created primary key used when not defining a primary key type.

Change in settings.py:
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
4. CSRF Verification Failed
Error Message: Forbidden (403) - CSRF verification failed.

Change in settings.py:
CSRF_TRUSTED_ORIGINS = ['https://*.replit.dev']
Restart the Django server after changes.
5. Missing Project Table in pyproject.toml
Error Message: No project table found in pyproject.toml.

Add [project] section in pyproject.toml:
[project]
name = "sandbox"
version = "0.1.0"
description = "A Django application for geospatial data management"
requires-python = ">=3.9"
dependencies = []
6. Conflicting Metadata Between pyproject.toml and setup.cfg
Error Message: Failed to build due to conflicting project metadata.

Changes Made:
Removed [project] section from pyproject.toml.
Final pyproject.toml:
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
Conclusion
After implementing the above commands and changes, run your commands again to ensure everything is functioning correctly. If issues persist, review each configuration and installation step one more time.

This note consolidates all the errors faced, the context in which they occurred, and the corresponding resolutions implemented to address them.


## Key Changes
- **GDAL** was installed using pre-built wheels to avoid `distutils` errors.
- Missing **django_deep_translator** dependency was installed.
- Static files were collected successfully after fixing dependencies.
- Changed static files storage to basic `StaticFilesStorage` to avoid source map issues.

## Issues Resolved
- **Initial `distutils` error** with GDAL installation.
- **Missing `django_deep_translator` module** error.
- **JSON editor source map processing error.**

Now the Django application should have all required dependencies and static files properly configured.


