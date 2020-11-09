from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.models import AfwasmiddelUser


class UserRegistrationTests(APITestCase):

    def setUp(self):
        # sample user
        self.test_data = {'email': 'test1@mail.com', 'username': 'DonaldTrump', 'password': 'fijeijafli123'}
        self.test_user1 = AfwasmiddelUser.objects.create_user(email=self.test_data['email'],
                                                              username=self.test_data['username'],
                                                              password=self.test_data['password'])
        self.url = reverse('account-create')

    def test_user_create(self):
        """
        Tests user creation with valid credentials
        201 is expected
        """
        data = {'email': 'test@gmail.com',
                'username': 'testuser',
                'password': 'debruinebar57'}

        response = self.client.post(path=self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data['username'], data['username'])
        self.assertEquals(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_user_email_already_exists(self):
        """
        Tests user creation with a email that already exists
        400 is expected.
        """
        data = self.test_data.copy()
        data['username'] = 'JoeBiden'
        response = self.client.post(path=self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_username_already_exist(self):
        """
        Tests user creation with a username that already exists
        400 is expected.
        """
        data = self.test_data.copy()
        data['email'] = 'fejifl@mail.com'
        response = self.client.post(path=self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
