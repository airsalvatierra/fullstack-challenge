#!/bin/sh
echo "makemigrations"
python manage.py makemigrations
echo "Apply database migrations"
python manage.py migrate
exec "$@"
