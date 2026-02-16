from django.test import TestCase
from django.urls import reverse


class StaticPagesTestCase(TestCase):
    """Test static pages (About, Services)"""

    def test_about_page_loads(self):
        """Test that the About page loads successfully"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Răzvan Ionescu")
        self.assertContains(response, "About Me")

    def test_services_page_loads(self):
        """Test that the Services page loads successfully"""
        response = self.client.get(reverse("services"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Services")
        self.assertContains(response, "Technology Consulting")

    def test_about_page_url(self):
        """Test that /about/ URL works"""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_services_page_url(self):
        """Test that /services/ URL works"""
        response = self.client.get("/services/")
        self.assertEqual(response.status_code, 200)
