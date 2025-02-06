# Use the official micromamba base image from mambaorg
FROM mambaorg/micromamba:1.5.0

# Port used by this container to serve HTTP
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    PATH="/opt/conda/bin:$PATH" \
    MAMBA_DOCKERFILE_ACTIVATE=1

# Install required system packages
USER root
RUN useradd wagtail && \
    apt-get update --yes --quiet && \
    apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    # Add these Cairo-related packages
    libcairo2-dev \
    libcairo2 \
    pkg-config \
    python3-cairo \
    cairo \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and set ownership of app directory
RUN mkdir /app && \
    chown wagtail:wagtail /app

# Set working directory
WORKDIR /app

# Switch to wagtail user for conda operations
USER wagtail

# Copy and install conda environment
COPY --chown=wagtail:wagtail environment.yml /app/environment.yml
RUN micromamba install -y -n base -f /app/environment.yml && \
    micromamba clean --all --yes

# Copy and install pip requirements
COPY --chown=wagtail:wagtail requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt && \
    pip install "gunicorn==20.0.4"

# Copy entrypoint script
USER root
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Copy the source code
COPY --chown=wagtail:wagtail . .

# Switch back to wagtail user for running the application
USER wagtail

# Collect static files
RUN python manage.py collectstatic --noinput --clear

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
#CMD set -xe; python manage.py migrate --noinput; gunicorn sandbox.wsgi:application

EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE="sandbox.sandbox.settings.production"
CMD ["gunicorn","--bind",":8000","--workers","2","sandbox.wsgi:application"]
