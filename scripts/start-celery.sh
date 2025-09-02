#!/bin/sh

set -e

echo "Waiting for postgres..."
/app/scripts/wait-for-postgres.sh $POSTGRES_HOST

echo "Starting Celery worker..."
celery -A notif_project worker -l info
