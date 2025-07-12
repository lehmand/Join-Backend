#!/usr/bin/env sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python create_guest_user.py
gunicorn --bind 0.0.0.0:8001 join_backend.wsgi:application