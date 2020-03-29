from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    brand = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category_choices = (
    ('DRINKS', 'Drinks'),
    ('SWEETENERS', 'Sweeteners'),
    ('SNACKS', 'Snacks'),
    ('SWEETS', 'Sweets'),
    ('FOOD', 'Food'),
    ('SUPPLEMENTS', 'Supplements'),
    )
    category = models.CharField(max_length=50, choices=category_choices, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name


class NutritionValue(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    calories_per_serving = models.DecimalField(max_digits=5, decimal_places=0)
    fat = models.CharField(max_length=10, default='')
    saturates = models.CharField(max_length=10, default='')
    carbs = models.CharField(max_length=10, default='')
    sugars = models.CharField(max_length=10, default='')
    polyols = models.CharField(max_length=10, default='')
    fibre = models.CharField(max_length=10, default='')
    protein = models.CharField(max_length=10, default='')
    salt = models.CharField(max_length=10, default='')
    
    def __str__(self):
        return self.product.name
    

class Ingredients(models.Model):
    name = models.CharField(max_length=75, default='')
    
    def __str__(self):
        return self.name


class ProductIngredients(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.product.name+ '-' +self.ingredient.name