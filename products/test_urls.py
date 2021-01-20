from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import all_products, product_detail


class TestUrls(SimpleTestCase):

    def test_houses_url_resolves(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, all_products)

    def test_house_info_url_resolves(self):
        url = reverse('product_detail', args=[1])
        self.assertEquals(resolve(url).func, product_detail)
