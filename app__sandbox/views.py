from django.shortcuts import render
from django.views.generic import DetailView, ListView

from app__recipe.models import Recipe


def index(request):
    return render(request, "app__sandbox/index.html", {})


class RecipeListView(ListView):
    model = Recipe
    template_name = "app__sandbox/index.html"
    context_object_name = "recipes"


class RecipeDetailView(DetailView):
    """View the detail of recipe"""

    model = Recipe
    template_name = "app__sandbox/recipe_detail.html"
    context_object_name = "recipe"
