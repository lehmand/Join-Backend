FROM python:3.13.5-slim-bookworm

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 8001

CMD ["/app/entrypoint.sh"]