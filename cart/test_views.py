from django.contrib.messages import get_messages
from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.cart_url = reverse('view_cart')
        Product.objects.create(
            name='test_product',
            price='10.99'
        )
        self.response = self.client.post(
            '/cart/add/1/', {
                'quantity': '7',
                'redirect_url': '/cart/'
            }
        )

    def test_cart_list_view(self):
        response = self.client.get(self.cart_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_cart_list_view_context(self):
        response = self.client.get(reverse('view_cart'))

        self.assertTrue('cart_items' in response.context)
        self.assertTrue('total' in response.context)
        self.assertTrue('product_count' in response.context)
        self.assertTrue('delivery' in response.context)
        self.assertTrue('grand_total' in response.context)
        self.assertFalse('random_field' in response.context)

    def test_add_to_view_cart(self):
        response = self.client.get(reverse('view_cart'))

        self.assertEqual(response.status_code, 200)

    def test_add_item_qty_to_add_cart_views(self):
        messages = list(get_messages(self.response.wsgi_request))

        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Added test_product to your cart'
        )

    def test_add_item_qty_to_add_cart_views_not_excisting_product_id(self):
        response = self.client.post(
            '/cart/add/2/', {
                'quantity': '7',
                'redirect_url': '/cart/'
            }
        )
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 404)
        # Only the one succesfull messages from the setUp
        self.assertEqual(len(messages), 1)

    def test_add_item_qty_to_adjust_cart_views(self):
        response = self.client.post(
            '/cart/adjust/1/', {'quantity': '10'})
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 302)
        # Two messages, first from the setUp add product
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         "Updated test_product quantity to 10")

    def test_remove_item_qty_to_adjust_cart_views(self):
        response = self.client.post(
            '/cart/adjust/1/', {'quantity': '1'})
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 302)
        # Two messages, first from the setUp add product
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         "Removed test_product quantity to 1")

    def test_remove_item_remove_cart_views(self):
        response = self.client.post(
            '/cart/remove/1/')
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 200)
        # Two messages, first from the setUp add product
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         "Removed test_product from your cart")
