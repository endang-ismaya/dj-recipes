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
            "image",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Recipe title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description",
                    "rows": "5",
                }
            ),
            "ingredients": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingredients",
                    "rows": "5",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
