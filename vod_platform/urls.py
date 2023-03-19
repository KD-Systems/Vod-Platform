from django.contrib import admin
from django.urls import path, include
from core.views import index

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),

    path("c/", include("channel.urls")),
    path("user/", include("userauths.urls")),
    # path("studio/", include("useradmin.urls")),
    # path("", index)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)