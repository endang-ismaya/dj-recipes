from django.shortcuts import render

from app__recipe.models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "app__recipe/recipes.html", context)


def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {"recipe": recipe}
    return render(request, "app__recipe/recipe.html", context)
