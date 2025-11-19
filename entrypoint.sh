#!/bin/bash
set -e  # exit on error.

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput --clear

exec gunicorn --bind 0.0.0.0:8001 barmichev.wsgi:application --workers 3 --timeout 60