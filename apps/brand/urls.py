from django.conf import settings
from django.urls import (
    path,
)
from django.conf.urls.static import static

from . import views
from brand.views import (
    IndexView,
    CreatePostView
)

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
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
    ),
    path(
        'created/',
        CreatePostView.as_view(),
        name = 'page_created'
    ),
    path(
        'brand/',
        views.brand,
        name = 'page_brand'
    )
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
