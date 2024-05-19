from django.urls import path

from app__sandbox import views

urlpatterns = [
    path("", views.RecipeListView.as_view(), name="app__sandbox_index"),
    path(
        "<int:pk>/",
        views.RecipeDetailView.as_view(),
        name="app__sandbox_recipe_detail",
    ),
    path(
        "homemades/",
        views.HomemadeListView.as_view(),
        name="app__sandbox_homemade",
    ),
    path("feedback/", views.feedback, name="app__sandbox_feedback"),
    path("thankyou/", views.thankyou, name="app__sandbox_thankyou"),
]
