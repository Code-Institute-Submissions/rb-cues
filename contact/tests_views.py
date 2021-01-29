from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):

    def test_Contact_get(self):
        resp = self.client.get(reverse('contact'))

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact/contact.html')
