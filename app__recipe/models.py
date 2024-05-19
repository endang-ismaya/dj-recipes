from django.contrib.auth.models import User
from django.db import models

from app__foodie.models import Category


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="recipe"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="recipe"
    )
    # date time creation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
