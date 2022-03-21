from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path(settings.ADMIN_SITE_URLS, admin.site.urls),
    path('',include('brand.urls')),
]+ static(
    settings.STATIC_URL,
    document_root = settings.STATIC_ROOT
)
