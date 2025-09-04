# Django Instant Notifications Project

## Installation
```
1- git clone -b dev https://github.com/deebajee2009/django_instant_notifications
2- cd django_instant_notifications

3- touch .env

# .env contents
POSTGRES_DB=notif_db_dev
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpassword

4- cd docker/dev
5- touch .env.dev

# .env.dev contents
DJANGO_SETTINGS_MODULE=core.settings.dev
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=-6-Kq(t@c@da$ro)p7&2v0-!u#k)s(_p^k!t(f^7q2!8#a#i-g
DJANGO_ALLOWED_HOSTS=localhost,web,*

POSTGRES_DB=notif_db_dev
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpassword
POSTGRES_HOST=postgres  # service name from docker-compose
POSTGRES_PORT=5432

REDIS_HOST=redis        # service name from docker-compose
REDIS_PORT=6379

6- cd ../..
7- chmod -x ./scripts/wait-for-postgres.sh

8- docker compose --project-directory . -f compose/docker-compose.yml -f docker/dev/docker-compose.override.yml up -d --build
```

## Message sending test
```
curl -X POST http://127.0.0.1:8000/send/ \
     -H "Content-Type: application/json" \
     -d '{
           "receivers": ["davood", "alireza"],
           "sender": "ادمین 1",
           "title": "درخواست مرخصی ساعتی",
           "text": "این یک پیام تستی است"
         }'
```
