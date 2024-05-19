from django.shortcuts import get_object_or_404, redirect, render

from app__foodie.forms import CategoryForm
from app__foodie.models import Category
from app__recipe.forms import RecipeForm
from app__recipe.models import Recipe


def index(request):
    """Homepage for Foodie"""
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "app__foodie/index.html", context)


def recipe_by_category(request, category_id):
    """URL for Recipe by Category"""
    recipes = Recipe.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)
    context = {"recipes": recipes, "category": category}
    return render(request, "app__foodie/recipes_by_category.html", context)


def add_category(request):
    """Adding a category to database"""
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("foodie:index")
        else:
            context = {"form": form}
            return render(request, "app__foodie/add_category.html", context)

    else:
        form = CategoryForm()
        context = {"form": form}

        return render(request, "app__foodie/add_category.html", context)


def add_recipe_by_category(request, category_id=None):
    category = None
    initial_data = {}

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        initial_data = {"category": category}

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, initial=initial_data)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            return redirect("recipe:index", category_id=new_recipe.category.id)
    else:
        form = RecipeForm(initial=initial_data)

    context = {"form": form, "category": category}
    return render(request, "app__foodie/add_recipe_by_cat.html", context)
