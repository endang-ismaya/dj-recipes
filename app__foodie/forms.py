from django import forms

from app__foodie.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        labels = {"name": "Category Name"}
