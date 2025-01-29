#!/bin/bash

# Create required directories
mkdir -p /home/app/static
mkdir -p /home/app/media

# Copy static files for mapviewer
mkdir -p /home/app/static/mapviewer
cp -r /app/.next/static/* /home/app/static/mapviewer/

# Start the mapviewer
yarn start
