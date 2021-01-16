#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput --traceback 2>&1

# Migrations could be run here, but that could be dangerous if there are not fully tested.
# Better to run them manually.
