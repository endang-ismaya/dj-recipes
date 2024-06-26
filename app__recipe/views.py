from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden
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


@login_required
def add_recipe(request):
    """Add recipe"""
    if request.method == "POST":
        form = RecipeForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            return redirect("recipe:index")

    else:
        form = RecipeForm()

    context = {"form": form}
    return render(request, "app__recipe/add_recipe.html", context)


def search_results(request):
    query = request.GET.get("query", "")

    results = (
        Recipe.objects.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(ingredients__icontains=query)
            | Q(directions__icontains=query)
            | Q(category__name__icontains=query)
        ).distinct()
        if query
        else []
    )
    # avoid duplicate results
    # seen_ids = set()
    # unique_results = []
    # for result in results:
    #     if result.id not in seen_ids:
    #         unique_results.append(result)
    #         seen_ids.add(result.id)

    # else:
    #     unique_results = []

    # results = Recipe.objects.filter(name__icontains=query) if query else []

    context = {"query": query, "results": results}
    return render(request, "app__recipe/search_result.html", context)


@login_required
def toggle_favorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.user in recipe.favorited_by.all():
        recipe.favorited_by.remove(request.user)
    else:
        recipe.favorited_by.add(request.user)
    return redirect("recipe:recipe", recipe_id=recipe_id)


@login_required
def favorite_recipes(request):
    user = request.user
    favorites = user.favorite_recipes.all()
    context = {"recipes": favorites}
    return render(request, "app__recipe/favorite_recipes.html", context)


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # check if the current user is the owner of the recipe or a superuser
    if not request.user == recipe.user and not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == "POST":
        recipe.delete()
        return redirect("recipe:index")

    context = {"recipe": recipe}
    return render(
        request, "app__recipe/recipe_confirmation_delete.html", context
    )


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if not request.user == recipe.user and not request.user.is_superuser:
        return HttpResponse("Not allowed.")
        # return HttpResponseForbidden()

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe:recipe", recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    context = {"form": form, "recipe": recipe}
    return render(request, "app__recipe/recipe_form.html", context)
