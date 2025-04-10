from decouple import config
from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

# Security setting
SECRET_KEY = config("SECRET_KEY")

# Debug should be False in production
DEBUG = False

# Your domain name 
DOMAIN = config("DOMAIN")

# Hosts/domain names that Django site can serve
ALLOWED_HOSTS = [
    DOMAIN,  # Allow domain and all subdomains
]

# CSRF Settings
CSRF_COOKIE_NAME = 'csrf_token' # Variable name to store CSRF token
CSRF_COOKIE_PATH = '/' # Set the path
CSRF_COOKIE_SECURE = True  # Only send CSRF cookie over HTTPS
CSRF_COOKIE_HTTPONLY = True  # JavaScript can't access CSRF cookie
CSRF_COOKIE_SAMESITE = 'Strict'  # Strict CSRF cookie policy
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN' # HTTP header name to send CSRF token
CSRF_TRUSTED_ORIGINS = [
    DOMAIN, # Trusted origins for CSRF
]
CSRF_USE_SESSIONS = True  # Store CSRF token in session instead of cookie

# Session Settings
SESSION_COOKIE_SECURE = True  # Only send session cookie over HTTPS
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access to session cookie
SESSION_COOKIE_SAMESITE = 'Strict'  # Strict same-site policy

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include subdomains in HSTS
SECURE_HSTS_PRELOAD = True  # Allow preloading of HSTS

# SSL/HTTPS Settings (Enable this setting in production)
# SECURE_SSL_REDIRECT = True  # Redirect all HTTP traffic to HTTPS
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Security Headers
SECURE_REFERRER_POLICY = 'same-origin'
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filtering
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing

# Cross-Origin Resource Sharing (CORS)
CORS_ALLOWED_ORIGINS = [
    DOMAIN,
]
CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']

# Add WhiteNoise middleware after SecurityMiddleware
MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware") # For serving static files

# Static files storage configuration
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "LOCATION": MEDIA_ROOT,  # Ensure MEDIA_ROOT is defined above
    },
}
