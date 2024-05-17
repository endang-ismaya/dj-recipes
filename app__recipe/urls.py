from django.urls import path

from app__recipe import views

urlpatterns = [path("", views.recipes, name="app__recipe_index")]
