from django.urls import path

from app__recipe import views

app_name = "recipe"

urlpatterns = [
    path("", views.recipes, name="index"),
    path("add/", views.add_recipe, name="add_recipe"),
    path("<int:recipe_id>/", views.recipe_detail, name="recipe"),
]
