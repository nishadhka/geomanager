# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.9.21-slim-bullseye

# Add user that will be used in the container.
RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install --find-links https://girder.github.io/large_image_wheels GDAL
RUN pip install "gunicorn==20.0.4"

# Create app directory
WORKDIR /app

# Copy requirements first for better cache utilization
COPY ./requirements.txt /app/requirements.txt

# Install the project requirements.
RUN pip install -r /app/requirements.txt

# Set this directory to be owned by the "wagtail" user.
RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Collect static files.
#RUN python manage.py collectstatic --noinput --clear

# Runtime command
#CMD set -xe; python manage.py migrate --noinput; gunicorn sandbox.wsgi:application
