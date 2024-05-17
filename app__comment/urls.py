from django.urls import path

from app__comment import views

urlpatterns = [path("", views.comments, name="app__comment_comments")]
