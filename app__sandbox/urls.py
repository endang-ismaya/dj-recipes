from django.urls import path

from app__sandbox import views

urlpatterns = [path("", views.index)]
