# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
# libpq-dev is for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    && apt-get clean

# Install dependencies
COPY ./requirements ./requirements
RUN pip install --upgrade pip && pip install -r ./requirements/dev.txt

# Copy project code
COPY . /app/

RUN chmod +x /app/scripts/wait-for-postgres.sh
