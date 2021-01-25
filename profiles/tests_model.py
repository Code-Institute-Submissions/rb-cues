from django.test import TestCase
from django.contrib.auth.models import User
from profiles.forms import UserProfileForm


class UserProfileTest(TestCase):

    def setUp(self):
        self.userprofile = User.objects.create_user(
            email='testing@testing.com',
            username='tester'
        )
        self.user = User.objects.get(id=1)

    def test_create_user(self):
        self.assertTrue(isinstance(self.userprofile, User))

    def test_user_string(self):
        userprofile = User.objects.get(id=1)
        self.assertEqual(userprofile.__str__(),  self.user.username)

    def test_user_profile_address_form_not_required(self):
        valid_data = {
            'default_email': '',
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_town_or_city': '',
            'default_postcode': '',
            'default_county': '',
            'default_country': ''
        }
        form = UserProfileForm(data=valid_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)
