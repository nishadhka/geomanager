#!/bin/bash
eval "$(micromamba shell hook --shell bash)"
micromamba activate base
#export $(flyctl secrets list | awk '{print $1}')
exec "$@"
