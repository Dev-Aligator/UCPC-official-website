#!/bin/sh

set -e

python3 /app/manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module ucpc.wsgi