from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from apps.home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
