from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    DRINKS = 'DR'
    SWEETENERS = 'SWTNR'
    SWEETS = 'SWTS'
    FOOD = 'FOOD'
    SUPPLEMENTS = 'SUPP'
    category_choices = (
    ('DRINKS', 'drinks'),
    ('SWEETENERS', 'sweeteners'),
    ('SWEETS', 'sweets'),
    ('FOOD', 'food'),
    ('SUPPLEMENTS', 'supplements'),
    )
    category = models.CharField(max_length=50, choices=category_choices)
    
    def __str__(self):
        return self.category in self.Product


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=254, default='')
    brand = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name


class NutritionValue(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    calories = models.DecimalField(max_digits=5, decimal_places=0)
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