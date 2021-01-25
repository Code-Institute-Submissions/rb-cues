from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestProfileViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="testuser",
            email="testuser@test.com",
            password="testing12345"
        )

    def test_logged_in_user_Profile_view_(self):
        user = self.client.login(
            email="testuser@test.com",
            password="testing12345"
        )
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="profiles/profile.html")

    def test_logged_in_user_Profile_context_(self):
        user = self.client.login(
            email="testuser@test.com",
            password="testing12345"
        )
        response = self.client.get(reverse('profile'))
        self.assertTrue('on_profile_page' in response.context)
        self.assertTrue('orders' in response.context)

    def test_logged_out_user_Profile_view_(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/profile/")
