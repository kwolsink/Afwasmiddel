from django.test import TestCase
from authentication import models as user_models


class UserModelTests(TestCase):

    def setUp(self):
        self.user_manager = user_models.AfwasmiddelUserManager()
        self.user_manager.model = user_models.AfwasmiddelUser
        self.test_username = 'test_user'
        self.test_email = 'test@test.com'
        self.test_password = 'wieditleesttrekteenspies123'

    def test_create_user_valid(self):
        user = self.user_manager.create_user(email=self.test_email, username=self.test_username,
                                             password=self.test_password)
        self.assertIsNotNone(user)
        self.assertEquals(user.username, self.test_username)
        self.assertEquals(user.email, self.test_email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user_valid(self):
        user = self.user_manager.create_superuser(email=self.test_email, username=self.test_username,
                                                   password=self.test_password)
        self.assertIsNotNone(user)
        self.assertEquals(user.username, self.test_username)
        self.assertEquals(user.email, self.test_email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_user_no_email(self):
        try:
            user = self.user_manager.create_user(email=None, username=self.test_username,
                                                 password=self.test_password)
            self.fail('User was successfully created even though no email was provided')
        except ValueError:
            pass

    def test_create_user_no_username(self):
        try:
            user = self.user_manager.create_user(email=self.test_email, username=None,
                                                 password=self.test_password)
            self.fail('User was successfully created even though no username was provided')
        except ValueError:
            pass
