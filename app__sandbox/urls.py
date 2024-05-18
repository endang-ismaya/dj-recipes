from django.urls import path

from app__sandbox import views

urlpatterns = [
    path("", views.RecipeListView.as_view(), name="app__sandbox_index")
]
