from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

user_model = get_user_model()


# LogoutView tests
class LogoutViewTest(TestCase):
    def setUp(self) -> None:
        user_model.objects.create_user(username='test_user', password='test_password')
        return super().setUp()

    def test_logout_view_success(self):
        # 1 - logout as authenticated user should redirect to homepage
        response = self.client.post(
            reverse('authentication:login'),
            {
                'username': 'test_user',
                'password': 'test_password'
            }
        )
        # check user is correctly authenticated
        self.assertEqual(response.status_code, 302)
        response = self.client.get(
            reverse('authentication:logout')
        )
        # check redirection to homepage
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home:homepage'))
        # check user is correctly deauthenticated
        response = self.client.get(
            reverse('authentication:login')
        )
        self.assertEqual(response.status_code, 200)

        # 2 - logout as not authenticated user should redirect to homepage
        response = self.client.get(
            reverse('authentication:logout')
        )
        # check redirection to homepage
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home:homepage'))
        # check user is still not authenticated
        response = self.client.get(
            reverse('authentication:login')
        )
        self.assertEqual(response.status_code, 200)
