from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Tests based on examples from class repo
class TestSnacks(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_page_templates(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')
        self.assertTemplateUsed(res, 'base.html')

    def test_about_page_status_code(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_about_page_templates(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'about.html')
        self.assertTemplateUsed(res, 'base.html')