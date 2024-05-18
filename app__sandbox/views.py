from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from app__recipe.models import Recipe


def index(request):
    return render(request, "app__sandbox/index.html", {})


class RecipeListView(ListView):
    model = Recipe
    template_name = "app__sandbox/index.html"
    context_object_name = "recipes"

    def get_queryset(self):
        """override queryset"""
        f_recipes = Recipe.objects.filter(category__name__iexact="chicken")
        return f_recipes


class RecipeDetailView(DetailView):
    """View the detail of recipe"""

    model = Recipe
    template_name = "app__sandbox/recipe_detail.html"
    context_object_name = "recipe"


class HomemadeListView(View):
    """Customize the view"""

    def get(self, request, *args, **kwargs):
        homemades = Recipe.objects.filter(description__icontains="homemade")
        context = {"homemades": homemades}

        return render(request, "app__sandbox/homemade_recipes.html", context)
