from django.test import TestCase
from django.urls import reverse

class CoreViewTests(TestCase):
    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_us(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_donate(self):
        response = self.client.get(reverse('donate'))
        self.assertEqual(response.status_code, 200)

    def test_types_of_abuse(self):
        response = self.client.get(reverse('types_of_abuse'))
        self.assertEqual(response.status_code, 200)

    def test_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
