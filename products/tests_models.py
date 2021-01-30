from django.test import TestCase
from products.models import Category, Product


class TestModels(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(
            name='Pool'
        )

        self.product1 = Product.objects.create(
            category=self.category1,
            sku='h202000001',
            name='LORUMIPSUM',
            description='LORUMIPSUM',
            price=222.00,
            stock=2
        )

    def test_city_is_assigned_name_on_creation(self):
        self.assertEquals(self.category1.name, 'Pool')

    def test_house_is_assigned_address_on_creation(self):
        self.assertEquals(self.product1.price, 222.00)
