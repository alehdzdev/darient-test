# -*- coding: utf-8 -*-
# Django
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.i18n import JavaScriptCatalog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Third Parties
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path(settings.ADMIN_PATH, admin.site.urls),
    re_path(r'^admin/jsi18n/', JavaScriptCatalog.as_view()),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('credits.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
