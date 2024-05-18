from django.shortcuts import render
from django.views.generic import ListView

from app__recipe.models import Recipe


def index(request):
    return render(request, "app__sandbox/index.html", {})


class RecipeListView(ListView):
    model = Recipe
    template_name = "app__sandbox/index.html"
    context_object_name = "recipes"
