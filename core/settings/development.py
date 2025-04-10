from decouple import config
from .base import *

# Security setting
SECRET_KEY = "dummy_secret123"

# Debug should be True in development
DEBUG = True

# Hosts/domain names that Django site can serve
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', "*"]