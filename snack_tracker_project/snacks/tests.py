from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class Test(TestCase):
    def test_snack_list_page(self):
        url=reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'snack_list.html')

