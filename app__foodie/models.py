from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    # date time creation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name