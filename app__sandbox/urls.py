from django.urls import path

from app__sandbox import views

app_name = "sandbox"

urlpatterns = [
    path("", views.RecipeListView.as_view(), name="index"),
    path(
        "<int:pk>/",
        views.RecipeDetailView.as_view(),
        name="recipe_detail",
    ),
    path(
        "homemades/",
        views.HomemadeListView.as_view(),
        name="homemade",
    ),
    path("feedback/", views.feedback, name="feedback"),
    path("thankyou/", views.thankyou, name="thankyou"),
]
