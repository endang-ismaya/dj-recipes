from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from _prj_foodie import settings

urlpatterns = [
    path("", include("app__foodie.urls")),
    path("recipes/", include("app__recipe.urls")),
    path("comments/", include("app__comment.urls")),
    path("admin/", admin.site.urls),
    path("sandbox/", include("app__sandbox.urls")),
    path("accounts/", include("app__account.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
