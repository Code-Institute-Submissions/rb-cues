from django.test import TestCase
from checkout.models import Order, OrderLineItem
from products.models import Product
from decimal import Decimal


class TestCheckoutModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        productcr = Product.objects.create(
            name='test_product',
            price='10'
        )

        ordercr = Order.objects.create(
            order_number=000,
            full_name='TestOrder',
            email='test@order.com',
            phone_number=987766544667,
            country='Nl',
            town_or_city='Town',
            street_address1='Street',
            order_total='10'
        )

        OrderLineItem.objects.create(
            order=ordercr,
            quantity=1,
            product=productcr,
            lineitem_total='10'
        )

    def test_Checkout_details(self):
        order = Order.objects.get(id=1)
        Order.update_total(order)
        Order.save(order)

        self.assertEqual(order.full_name, 'TestOrder')
        self.assertEqual(order.email, 'test@order.com')
        self.assertEqual(order.town_or_city, 'Town')
        self.assertEqual(order.order_total, 10)
        # Delivery costs added
        self.assertEqual(order.delivery_cost, round(Decimal(5.99), 2))
        self.assertEqual(order.grand_total, round(Decimal(15.99), 2))

    def test_Checkout_generate_order_number(self):
        order = Order.objects.get(id=1)
        self.assertFalse(order.order_number == 000)
