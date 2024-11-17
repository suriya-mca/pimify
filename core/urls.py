from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from api.main import app

urlpatterns = [
    path('', lambda request: redirect('dashboard/', permanent=True)),
    path('dashboard/', admin.site.urls),
    path('api/v1/', app.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)