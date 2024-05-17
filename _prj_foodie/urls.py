from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("app__foodie.urls")),
    path("admin/", admin.site.urls),
    path("sandbox/", include("app__sandbox.urls")),
]
