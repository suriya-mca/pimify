import multiprocessing

# Server socket configuration
bind = '0.0.0.0:8000'
backlog = 2048  # Number of pending connections queue will hold

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 4
worker_connections = 1000
max_requests = 10000
max_requests_jitter = 1000  # Prevents all workers from restarting at once

# Timeouts
timeout = 60
graceful_timeout = 30
keepalive = 5

# Security
limit_request_line = 4096
limit_request_fields = 100
limit_request_field_size = 8190

# Enable access and error logging
accesslog = '-'  # Log access to stdout
errorlog = '-'   # Log errors to stdout
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s'

# Recommended: Run Gunicorn behind a reverse proxy like NGINX
# proxy_protocol = True

# Process naming
proc_name = "gunicorn_app"