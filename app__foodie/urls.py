from django.urls import path

from app__foodie import views

app_name = "foodie"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "categories/add/",
        views.add_category,
        name="add_category",
    ),
    path(
        "categories/category/<int:category_id>/",
        views.add_recipe_by_category,
        name="add_recipe_with_genre",
    ),
    path(
        "categories/<int:category_id>/",
        views.recipe_by_category,
        name="recipe_by_category",
    ),
]
