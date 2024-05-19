from django.shortcuts import redirect, render

from app__recipe.forms import RecipeForm
from app__recipe.models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "app__recipe/recipes.html", context)


def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {"recipe": recipe}
    return render(request, "app__recipe/recipe.html", context)


def add_recipe(request):
    """Add recipe"""
    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("app__recipe_index")

    else:
        form = RecipeForm()

    context = {"form": form}
    return render(request, "app__recipe/add_recipe.html", context)
