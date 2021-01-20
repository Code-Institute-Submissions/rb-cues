from django.contrib import admin
from .models import Product, Category

# Class for the representation of the product model in the Django admin section
class ProductAdmin(admin.ModelAdmin):
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

# Class for the representation of the category model in the Django admin section
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
