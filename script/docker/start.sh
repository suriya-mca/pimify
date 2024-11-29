#!/bin/sh

python manage.py collectstatic --noinput

echo "Superuser created with username 'admin' and password 'admin123'"
echo "**IMPORTANT:** Change the password immediately after logging in for the first time."

gunicorn core.wsgi:application -c /etc/gunicorn/gunicorn.conf.py