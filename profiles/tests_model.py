from django.test import TestCase
from django.contrib.auth.models import User


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
