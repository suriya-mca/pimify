#!/bin/sh

python manage.py migrate
python manage.py makemigrations api
python manage.py migrate

python manage.py collectstatic --noinput

mkdir -p data
mkdir -p media

python manage.py createsuperuser

gunicorn core.wsgi:application -c /etc/gunicorn/gunicorn.conf.py