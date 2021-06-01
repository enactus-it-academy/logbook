from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from account.models import User


class AccountTests(APITestCase):
    """Ensure we can create a new account object."""

    user_list_url = reverse('user-list')
    user_me_url = reverse('user-me')
    jwt_create_url = reverse('jwt-create')

    def setUp(self):
        self.user_data = {
            'username': 'owner-1',
            'password': 'michael-1958',
        }

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)

    def jwt_create(self):
        response = self.client.post(self.jwt_create_url, self.user_data)
        self.token = response.data['access']

    def test_create_owner_account(self):
        self.user_data.update({'is_owner': 'True'})
        response = self.client.post(self.user_list_url, self.user_data)
        user = User.objects.get()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.is_owner, True)
        self.assertEqual(user.owner.id, 1)

    def test_create_employee_account(self):
        self.user_data.update({'is_owner': 'False'})
        response = self.client.post(self.user_list_url, self.user_data)
        user = User.objects.get()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.is_owner, False)
        self.assertEqual(user.employee.id, 1)

    def test_user_profile(self):
        self.client.post(self.user_list_url, self.user_data)
        self.jwt_create()
        self.api_authentication()
        response = self.client.get(self.user_me_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
