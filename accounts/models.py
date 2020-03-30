from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    telephone = models.IntegerField(default='', blank=False)
    address_1 = models.CharField(max_length=75, default='', blank=False)
    address_2 = models.CharField(max_length=75, default='', blank=True)
    city = models.CharField(max_length=75, default='', blank=False)
    county = models.CharField(max_length=75, default='', blank=True)
    postcode = models.CharField(max_length=8, default='', blank=False)
    dietary_choices = (
    ('NONE', 'None'),
    ('VEGETARIAN', 'Vegetarian'),
    ('VEGAN', 'Vegan'),
    ('PESCETARIAN', 'Pescetarian'),
    ('KOSHER', 'Kosher'),
    ('HALAL', 'Halal'),
    )
    dietary_preference = models.CharField(max_length=50, choices=dietary_choices, null=True, blank=False)
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
    allegeries_intolerances = models.CharField(max_length=50, choices=allegeries_intolerances_choices, null=True, blank=False)
    
    def __str__(self):
        return self.user.username