from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("app__foodie.urls")),
    path("recipes/", include("app__recipe.urls")),
    path("comments/", include("app__comment.urls")),
    path("admin/", admin.site.urls),
    path("sandbox/", include("app__sandbox.urls")),
    path("accounts/", include("app__account.urls")),
]
