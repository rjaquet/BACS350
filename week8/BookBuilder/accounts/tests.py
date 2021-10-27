from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


def create_test_user():
    return get_user_model().objects.create_user(username='TEST_DUDE', email='me@here.com', password='secret', first_name='Testy', last_name='Sensei')


class TestAccountsData(TestCase):

    def test_accounts(self):
        user = create_test_user()
        self.assertEqual(user.email, 'me@here.com')
        self.assertEqual(len(User.objects.all()), 1)

    def test_string(self):
        user = create_test_user()
        self.assertEqual(str(user), 'TEST_DUDE')


class TestAccountsViews(TestCase):

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/book/')

        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme.html')

    def test_login_view(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/accounts/login/')

        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme.html')

    def test_logout_view(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home'))

    def test_signup_view(self):
        response = self.client.get('/accounts/signup')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, reverse('signup'))

        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme.html')
