from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.urls.conf import re_path
from project.settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static

from apps.home.views import *

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    
    # INCLUDE APPS
    path('', include('home.urls')),
]

# INCLUDE STATIC
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if DEBUG:
    import debug_toolbar 
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]