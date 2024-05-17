from django.contrib import admin

from app__recipe.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "description",
        "ingredients",
        "directions",
        "category",
        "created_at",
        "updated_at",
    )
    search_fields = ("name",)


admin.site.register(Recipe, RecipeAdmin)
