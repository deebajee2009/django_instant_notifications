# django_instant_notifications

cd myproject/compose
docker compose --project-directory . -f compose/docker-compose.yml -f docker/dev/docker-compose.override.yml up -d --build

# .env example
POSTGRES_DB=notif_db_dev
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpassword

# .env.dev example
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
