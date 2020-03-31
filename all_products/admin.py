from django.contrib import admin
from .models import Product, NutritionValue, Ingredients, ProductIngredients

admin.site.register(Product)
admin.site.register(NutritionValue)
admin.site.register(Ingredients)
admin.site.register(ProductIngredients)