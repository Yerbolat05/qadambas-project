from django.conf import settings
from django.urls import (
    path,
)
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name = 'page_main'
    ),
    path(
        'login/',
        views.login,
        name = 'page_login'
    ),
    path(
        'register/',
        views.register,
        name = 'page_register'
    ),
    path(
        'logout/',
        views.logout,
        name = 'page_logout'
    )
]+static(settings.STATIC_URL,documennt_root=settings.STATIC_ROOT)
