#!/bin/bash

cd /app/
echo "Apply database migrations"
python manage.py migrate --noinput

#echo "collect static"
#python manage.py collectstatic --noinput
#
#echo "createsuperuser"
#python manage.py createsuperuser --noinput \
#      --username $DJANGO_SUPERUSER_USERNAME \
#      --email $DJANGO_SUPERUSER_EMAIL

echo "creating log dir if not exist"
mkdir -p /var/log/gunicorn
mkdir -p /var/log/telegram_bot

echo "Starting telegram bot app"
python manage.py telegram_bot &

echo "Starting django app"
gunicorn stand_bot.wsgi:application --bind 0.0.0.0:8000 \
    --access-logfile /var/log/gunicorn/access.log \
    --error-logfile /var/log/gunicorn/error.log