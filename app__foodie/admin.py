from django.contrib import admin

from app__foodie.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    search_help_text = "Write in your query and hit enter"


admin.site.register(Category, CategoryAdmin)
