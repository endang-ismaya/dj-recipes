from django.contrib.auth.models import User
from django.db import models

from app__recipe.models import Recipe


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="comments"
    )
    # date time creation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.name}"
