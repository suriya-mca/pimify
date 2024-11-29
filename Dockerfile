FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PIP_NO_CACHE_DIR 1

WORKDIR /app

COPY . /app
COPY ./data /data
COPY ./script/gunicorn/gunicorn.conf.py /etc/gunicorn/gunicorn.conf.py

RUN chmod +x /app/script/docker/start.sh && \
    pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt && \
    python manage.py migrate && \
    python manage.py makemigrations api && \
    python manage.py migrate

ENTRYPOINT ["sh", "-c", "./script/docker/start.sh"]