#!/bin/bash

# migrate db
python sandbox/manage.py migrate --noinput

# collect static files
python sandbox/manage.py collectstatic --clear --no-input

# create geomanager auto-ingest data dir
export GEOMANAGER_AUTO_INGEST_RASTER_DATA_DIR=${GEOMANAGER_AUTO_INGEST_RASTER_DATA_DIR:-/geomanager/data}
