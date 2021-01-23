from django.test import TestCase, Client
from django.urls import reverse
from checkout.models import Order
from .forms import OrderForm


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')
        Order.objects.create(
            order_number='test1234',
            order_total='10.99'
        )
        form_data = {
            'full_name': 564356456456
        }

    def test_Checkout_get(self):
        resp = self.client.get(reverse('checkout'))

        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, "/products/")

    def test_Checkout_out_success_view(self):
        order = Order.objects.get(id=1)
        order_num = order.order_number

        resp = self.client.get(
            f'/checkout/checkout_success/{order_num}')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'checkout/checkout_success.html')

    def test_cache_checkout_data_get(self):
        resp = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(resp.status_code, 405)
