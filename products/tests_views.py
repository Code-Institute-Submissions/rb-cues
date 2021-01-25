from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')
        User.objects.create_user(
            username="tester",
            email="testing@test.com",
            password="testing12345"
        )
        Product.objects.create(
            name='test_product',
            price='10.99',
            new=True,
            deal=True
        )

    def test_view_products_GET(self):
        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_views_contains_products_GET(self):
        product = Product.objects.get(id=1)
        response = self.client.get(reverse('products'))

        self.assertContains(response, product.name)

    def test_product_sort_name_asc_post(self):
        response = self.client.get(
            '/products/?', {'sort': 'name', 'direction': 'asc'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_sorting'], 'name_asc')

    def test_product_sort_name_desc_post(self):
        response = self.client.get(
            '/products/?', {'sort': 'name', 'direction': 'desc'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_sorting'], 'name_desc')

    def test_product_sort_category_asc_post(self):
        response = self.client.get(
            '/products/?', {'sort': 'category', 'direction': 'asc'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_sorting'], 'category_asc')

    def test_product_sort_category_desc_post(self):
        response = self.client.get(
            '/products/?', {'sort': 'category', 'direction': 'desc'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_sorting'], 'category_desc')

    def test_product_sort_price_asc_post(self):
        response = self.client.get(
            '/products/?', {'sort': 'price', 'direction': 'asc'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_sorting'], 'price_asc')

    def test_product_sort_price_desc_post(self):
        response = self.client.get(
            '/products/?', {'sort': 'price', 'direction': 'desc'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_sorting'], 'price_desc')

    def test_product_search_post(self):
        response = self.client.get(
            '/products/?', {'q': 'jeans'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_term'], 'jeans')

    def test_product_search_Error_message_post(self):
        response = self.client.get(
            '/products/?', {'q': ''})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "You didn't enter any search criteria!"
        )

    def test_product_new_post(self):
        response = self.client.get(
            '/products/?new')
        self.assertEqual(response.status_code, 200)
        product = Product.objects.get(id=1)

        # No context due to seperate page
        self.assertEqual(response.context['current_sorting'], 'None_None')
        self.assertContains(response, product.name)
