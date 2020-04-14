from django.test import TestCase
from .models import Product

class TestProductViews(TestCase):
    def test_products_page_can_be_viewed(self):
        page=self.client.get('/all_products/')
        self.assertEqual(page.status_code, 200)
        self.assertNotEqual(page.status_code, 404)