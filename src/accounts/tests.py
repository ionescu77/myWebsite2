from django.contrib.auth import authenticate, login

from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.utils.encoding import smart_text as smart_unicode

from django.test import TestCase, LiveServerTestCase, Client

from django.utils import timezone
from blogengine.models import Post, Category, Tag
import markdown2 as markdown
import feedparser
import factory.django

from django.contrib.auth.models import User

# Create your tests here.

class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

class AccountsTest(BaseAcceptanceTest):
    # We need to fill the auth database for login test
    # python manage.py dumpdata auth.User --indent=2 > blogengine/fixtures/users.json
    fixtures = ['users.json']

    def setUp(self):
        # Create client
        self.client = Client()
        # Create user
        self.credentials = {
            'username': 'abhishek',
            'password': 'Abhishek@12345'}
        User.objects.create_user(**self.credentials)


    def test_login(self):
        with self.settings(AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.ModelBackend',]):
            # Get login page
            response = self.client.get('/mylogin/', follow=True)
            # send login data
            response = self.client.post('/mylogin/', self.credentials, follow=True)
            # should be logged in now
            print(response.context['user'])
            self.assertTrue(response.context['user'].is_authenticated)
            print (response)
            # Check response code Django does redirect on Admin so code 302, we need to set follow=True
            self.assertEquals(response.status_code, 200)
            # Check 'Username' in login form webpage
            self.assertTrue(b'Username' in response.content)
            # Check 'asteriskField' in login form webpage
            self.assertTrue(b'asteriskField' in response.content)
            # Check 'glyphicon-lock' in webpage which means not authenticated
            self.assertTrue(b'glyphicon-lock' in response.content)
            # Log the user in
            self.client.login(username='testuser', password='test')
            # Check response code
            response = self.client.get('/mylogin/')
            self.assertEquals(response.status_code, 200)
            # Check 'glyphicon-flash' in webpage which means authenticated
            self.assertTrue(b'glyphicon-flash' in response.content)

    def test_logout(self):
        with self.settings(AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.ModelBackend',]):
            # Login
            self.client.login(username='testuser', password='test')
            # Check response code
            response = self.client.get('/mylogin/')
            print(response)
            self.assertEquals(response.status_code, 200)
            # Check 'glyphicon-flash' in webpage which means authenticated
            self.assertTrue(b'glyphicon-flash' in response.content)
            # Log out
            self.client.logout()
            # Check response code
            response = self.client.get('/mylogout/', follow=True)
            self.assertEquals(response.status_code, 200)
            # Check 'glyphicon-lock' in webpage which means not authenticated
            self.assertTrue(b'glyphicon-lock' in response.content)
