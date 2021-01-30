from django.db import models


# A model for the categories
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# A model for the products
class Product(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(
        max_length=254, null=True, blank=True
    )
    name = models.CharField(
        max_length=254
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2
    )
    image = models.ImageField(
        null=True, blank=True
    )
    stock = models.DecimalField(
        max_digits=6, decimal_places=0, default=0
    ) 
    new = models.BooleanField(
        null=False, blank=False, default=False
    )
    deal = models.BooleanField(
        null=False, blank=False, default=False
    )

    def __str__(self):
        return self.name
