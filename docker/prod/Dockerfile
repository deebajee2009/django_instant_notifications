# --- Builder Stage ---
FROM python:3.10-slim-buster AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential

# Install python dependencies
COPY ./requirements .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r /requirements/prod.txt


# --- Final Stage ---
FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y libpq-dev netcat-traditional && apt-get clean

# Copy pre-built wheels and install them
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy scripts and make them executable
COPY ./scripts/ /app/scripts/
RUN chmod +x /app/scripts/*.sh

# Copy application code
COPY . .

# Set entrypoint
ENTRYPOINT ["/app/scripts/entrypoint.sh"]
