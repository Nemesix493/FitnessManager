from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

user_model = get_user_model()


# LoginView tests
class LoginViewTest(TestCase):
    def setUp(self) -> None:
        user_model.objects.create_user(username='test_user', password='test_password')
        return super().setUp()

    def test_login_view_success(self):
        # 2 - login as not authenticated user should authenticate and redirect to hompage
        response = self.client.post(
            reverse('authentication:login'),
            {
                'username': 'test_user',
                'password': 'test_password'
            }
        )
        self.assertEqual(response.status_code, 302)
        # check redirection to the right page
        self.assertEqual(response.url, reverse('home:homepage'))

        # 2 - login as authenticated user should redirect to hompage
        response = self.client.get(
            reverse('authentication:login'),
        )
        self.assertEqual(response.status_code, 302)
        # check redirection to the right page
        self.assertEqual(response.url, reverse('home:homepage'))

    def test_login_view_error(self):
        # wrong password should return 200
        response = self.client.post(
            reverse('authentication:login'),
            {
                'username': 'test_user',
                'password': 'wrong_test_password'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password.')
        # wrong username should return 200
        response = self.client.post(
            reverse('authentication:login'),
            {
                'username': 'wrong_test_user',
                'password': 'test_password'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password.')
