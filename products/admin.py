from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "year",
        "price",
        "user",
        "is_published",
        "created_at",
    )

    list_display_links = ("id", "name")

    search_fields = ("name",)

    list_filter = ("year", "user", "is_published")

    list_editable = ("is_published",)

    list_per_page = 10

    ordering = ("-created_at",)