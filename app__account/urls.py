from django.urls import include, path

from app__account import views

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.user_register, name="register"),
]
