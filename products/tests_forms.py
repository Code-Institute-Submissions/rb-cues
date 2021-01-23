from django.test import TestCase
from products.forms import ProductForm


class TestProductForm(TestCase):

    def test_rating_is_required(self):
        form = ProductForm({'rating': ''})
        self.assertFalse(form.is_valid())

    def test_content_is_required(self):
        form = ProductForm({'content': 'Testing Context'})
        self.assertTrue(form.is_valid)

    def test_product_comment_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, ('__all__'))
