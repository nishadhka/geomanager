# Deployment Guide

## Replit Deployment Steps

1. **Environment Setup**
   ```bash
   # Initialize micromamba environment
   eval "$(micromamba shell hook --shell=bash)"
   micromamba create -n replit-env
   micromamba activate replit-env
   ```

2. **Install Dependencies**
   ```bash
   # Install required packages
   micromamba install -y -c conda-forge python=3.9 gdal proj geos
   micromamba install -y -c conda-forge numpy=1.21.6 pandas=1.4.4
   ```

3. **Deploy**
   ```bash
   python manage.py collectstatic --noinput
   gunicorn --config gunicorn_config.py sandbox.wsgi:application
   ```

## Fly.io Deployment Steps

1. **Install Fly CLI**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Configure Project**
   - Create `Dockerfile`:
   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["gunicorn", "sandbox.wsgi:application"]
   ```

3. **Deploy to Fly.io**
   ```bash
   fly auth login
   fly launch
   fly deploy
   ```

4. **Set Environment Variables**
   ```bash
   fly secrets set SECRET_KEY="your-secret-key"
   fly secrets set DJANGO_SETTINGS_MODULE="sandbox.settings.production"
   ```

## Common Troubleshooting

- For static files issues: `python manage.py collectstatic --noinput --clear`
- Check logs: `fly logs`
- Verify GDAL: `python -c "from osgeo import gdal; print(gdal.__version__)"`
- Debug mode: Set `DEBUG=True` in settings temporarily
