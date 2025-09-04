#!/bin/sh

set -e

echo "Waiting for postgres..."
/app/scripts/wait-for-postgres.sh $POSTGRES_HOST

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Execute the command passed to this script
exec "$@"
