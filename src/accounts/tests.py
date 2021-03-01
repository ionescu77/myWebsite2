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

    def test_login(self):
        with self.settings(AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.ModelBackend',]):
            # Get login page
            response = self.client.get('/mylogin/', follow=True)
            # Check response code Django does redirect on Admin so code 302, we need to set follow=True
            self.assertEquals(response.status_code, 200)
            # Check 'Log in' in admin webpage
            self.assertTrue(b'Log in' in response.content)
            # Log the user in
            self.client.login(username='testuser', password='test')
            # Check response code
            response = self.client.get('/mylogin/')
            self.assertEquals(response.status_code, 200)
            # Check 'Log out' in response
            self.assertTrue(b'Log out' in response.content)

    def test_logout(self):
        with self.settings(AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.ModelBackend',]):
            # Login
            self.client.login(username='testuser', password='test')
            # Check response code
            response = self.client.get('/mylogout/')
            self.assertEquals(response.status_code, 200)
            # Check 'Log out' in response
            self.assertTrue(b'Log out' in response.content)
            # Log out
            self.client.logout()
            # Check response code
            response = self.client.get('/mylogout/', follow=True)
            self.assertEquals(response.status_code, 200)
            # Check 'Log in' in response
            self.assertTrue(b'Log in' in response.content)
