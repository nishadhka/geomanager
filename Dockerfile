# Use the official micromamba base image from mambaorg
FROM mambaorg/micromamba:1.5.0

# Add user that will be used in the container.
#RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Add after the ENV section:
ENV PATH="/opt/conda/bin:$PATH"

# Install required system packages including build-essential (which provides gcc)
USER root

RUN useradd wagtail

#RUN apt-get update && apt-get install -y build-essential && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*


# Set working directory and enable auto-activation of the base environment
WORKDIR /app
ENV MAMBA_DOCKERFILE_ACTIVATE=1

USER wagtail 
# Copy the conda environment file
COPY environment.yml /app/environment.yml

# Install the application server.
# Create the conda environment (named "myenv") and clean up caches.
RUN micromamba install -y -n base -f /app/environment.yml && \
    micromamba clean --all --yes

# Copy your pip requirements
COPY requirements.txt /app/requirements.txt

# Install the remaining Python pac:e kages using pip.
# Make sure that none of these conflict with the conda-installed packages.
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install "gunicorn==20.0.4"

# Add before the final CMD (if any):
#COPY entrypoint.sh /usr/local/bin/
#RUN chmod +x /usr/local/bin/entrypoint.sh
#ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
#CMD ["/bin/bash"]
# Switch to root for copying and setting permissions
USER root
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Switch back to wagtail user
USER wagtail
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/bin/bash"]
# Copy the rest of your application source code
#COPY . /app

# Expose the port used by your Django application (adjust as needed)
#EXPOSE 8000

# Run migrations, collect static files if needed, and start the application server.
#CMD ["gunicorn", "myproject.wsgi:application"]
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
RUN python manage.py collectstatic --noinput --clear

# Runtime command
CMD set -xe; python manage.py migrate --noinput; gunicorn sandbox.wsgi:application
