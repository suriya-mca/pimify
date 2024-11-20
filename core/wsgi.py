import os
from django.core.wsgi import get_wsgi_application  

# Set the Django settings file.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Create the WSGI application.
application = get_wsgi_application()

