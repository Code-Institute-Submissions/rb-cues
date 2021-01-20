from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')

    def test_view_products_GET(self):
        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
