FROM python:3.12-alpine

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PATH="/home/appuser/.local/bin:$PATH"

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory and copy files
WORKDIR /app
COPY . /app
COPY ./script/gunicorn/gunicorn.conf.py /etc/gunicorn/gunicorn.conf.py

# Set permissions for the app directory and required folders
RUN mkdir -p /app/data /app/backups /app/media && \
    chown -R appuser:appgroup /app /etc/gunicorn && \
    chmod -R 755 /app/data /app/backups /app/media

# Switch to non-root user
USER appuser

# Install dependencies and make install script executable
RUN chmod +x /app/install.oci.sh

# Set entrypoint
CMD ["sh", "install.oci.sh"]
