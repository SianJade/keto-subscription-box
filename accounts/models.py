from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    dietary_choices = (
    ('NONE', 'None'),
    ('VEGETARIAN', 'Vegetarian'),
    ('VEGAN', 'Vegan'),
    ('PESCETARIAN', 'Pescetarian'),
    ('KOSHER', 'Kosher'),
    ('HALAL', 'Halal'),
    )
    dietary_preference = models.CharField(max_length=50, choices=dietary_choices)
    allegeries_intolerances_choices = (
    ('NONE', 'None'),
    ('NUTS', 'Nuts'),
    ('Milk', 'Milk'),
    ('LACTOSE', 'Lactose'),
    ('EGG', 'Egg'),
    ('FISH', 'Fish'),
    ('SHELLFISH', 'Shellfish'),
    ('GLUTEN', 'Gluten'),
    ('SOY', 'Soy'),
    ('WHEAT', 'Wheat'),
    )
    allegeries_intolerances = models.CharField(max_length=50, choices=allegeries_intolerances_choices)
    
    def __str__(self):
        return self.user.username