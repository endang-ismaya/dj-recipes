from django.urls import path

from app__comment import views

app_name = "comment"

urlpatterns = [path("", views.comments, name="comments")]
