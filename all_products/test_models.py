from django.test import TestCase
from .models import Product


class TestProductCreation(TestCase):
    def test_product_creation(self):
        # assertions are listed in the order in which the fields appear in the Product model
        product = Product(name='New Product',
                        description='A tasty beverage',
                        price='1.99')
        self.assertEqual(product.name, 'New Product')
        self.assertFalse(product.brand)
        self.assertEqual(product.description, 'A tasty beverage')
        self.assertEqual(product.price, '1.99')
        self.assertFalse(product.category)
        self.assertFalse(product.image)