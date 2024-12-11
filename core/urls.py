# Import necessary modules
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from api.management.commands import scheduler
from api.main import app

urlpatterns = [
    # Redirect root URL to dashboard
    path('', lambda request: redirect('dashboard/', permanent=True)),
    
    # Admin dashboard URL (using Django's admin site)
    path('dashboard/', admin.site.urls),
    
    # API endpoints (version 1)
    path('api/v1/', app.urls),
]

# # Only start the scheduler if the OPEN_EXCHANGE_RATES_APP_ID is set
# if getattr(settings, 'OPEN_EXCHANGE_RATES_APP_ID', None):
#     scheduler.start()
# else:
#     print("OPEN_EXCHANGE_RATES_APP_ID is not set. Scheduler will not start.")

# Serve static and media files in development
if settings.DEBUG:
    # Serve static files (CSS, JavaScript, etc.)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Serve media files (user-uploaded content)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)