from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Class for the representation of the
    product model in the Django admin section
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'deal',
        'new',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Class for the representation of the
    category model in the Django admin section
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
