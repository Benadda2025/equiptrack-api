FROM mcr.microsoft.com/devcontainers/python:3.12

# System deps: Postgres client tools for psql / pg_isready
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends postgresql-client libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
