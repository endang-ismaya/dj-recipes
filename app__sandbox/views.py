from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView

from app__recipe.models import Recipe
from app__sandbox.forms import FeedbackForm
from app__sandbox.models import Feedback


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


def feedback(request):
    """Feedback View"""
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # process the form
            print(form.cleaned_data)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            feedback = form.cleaned_data["feedback"]
            satisfaction = form.cleaned_data["satisfaction"]
            Feedback.objects.create(
                name=name,
                email=email,
                feedback=feedback,
                satisfaction=satisfaction,
            )
            return redirect("app__sandbox_thankyou")
        else:
            context = {"form": form}
            return render(request, "app__sandbox/feedback.html", context)
    else:
        form = FeedbackForm()
        context = {"form": form}
        return render(request, "app__sandbox/feedback.html", context)


def thankyou(request):
    return HttpResponse("Thank you for your feedback!.")
