from django import forms

from app__recipe.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            "name",
            "description",
            "ingredients",
            "directions",
            "category",
        )
