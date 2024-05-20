from django.shortcuts import get_object_or_404, redirect, render

from app__comment.forms import CommentForm
from app__recipe.forms import RecipeForm
from app__recipe.models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "app__recipe/recipes.html", context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    comments = recipe.comments.all()

    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.recipe = recipe
            new_comment.save()

            return redirect(recipe.get_absolute_url())

    else:
        comment_form = CommentForm()

    context = {
        "recipe": recipe,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "app__recipe/recipe.html", context)


def add_recipe(request):
    """Add recipe"""
    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            return redirect("recipe:index")

    else:
        form = RecipeForm()

    context = {"form": form}
    return render(request, "app__recipe/add_recipe.html", context)
