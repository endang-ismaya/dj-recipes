from django.urls import path

from app__foodie import views

urlpatterns = [
    path("", views.index, name="app__foodie_index"),
    path(
        "categories/add/",
        views.add_category,
        name="app__foodie_add_category",
    ),
    path(
        "categories/<int:category_id>/",
        views.recipe_by_category,
        name="app__foodie_categories",
    ),
]
