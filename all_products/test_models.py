from django.test import TestCase
from .models import Product, NutritionValue, Ingredients, ProductIngredients


class TestProductCreation(TestCase):
    def test_product_creation(self):
        """
        Assertions are listed in the order in which
        the fields appear in the Product model
        """
        product = Product(name='New Product',
                          description='A tasty beverage',
                          price='1.99')
        self.assertEqual(product.name, 'New Product')
        self.assertFalse(product.brand)
        self.assertEqual(product.description, 'A tasty beverage')
        self.assertEqual(product.price, '1.99')
        self.assertFalse(product.category)
        self.assertFalse(product.image)


class TestNutritionValues(TestCase):
    def test_nutrition_values(self):
        """
        Assertions are listed in the order in which
        the fields appear in the NutritionValue model
        """
        nutrition = NutritionValue(calories_per_serving='123',
                                   carbs='2.4',
                                   sugars='2',
                                   salt='0.01')
        self.assertNotEqual(nutrition.calories_per_serving, '250')
        self.assertFalse(nutrition.fat)
        self.assertFalse(nutrition.saturates)
        self.assertEqual(nutrition.carbs, '2.4')
        self.assertNotEqual(nutrition.sugars, '1.2')
        self.assertFalse(nutrition.polyols)
        self.assertFalse(nutrition.fibre)
        self.assertFalse(nutrition.protein)
        self.assertEqual(nutrition.salt, '0.01')


class TestIngredientModel(TestCase):
    def test_ingredients(self):
        ingredient = Ingredients(name='baking powder')
        self.assertEqual(ingredient.name, 'baking powder')
        self.assertNotEqual(ingredient.name, 'flour')
