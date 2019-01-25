from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("api/v1/", include("core.api.urls")),
    path("drf/api/", include("rest_framework.urls")),
]
