from django.http import HttpResponse

from app__recipe.models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return HttpResponse("Recipe Page")
