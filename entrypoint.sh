#!/usr/bin/env sh

python manage.py makemigrations
python manage.py migrate
python create_guest_user.py
python manage.py runserver 0.0.0.0:8001