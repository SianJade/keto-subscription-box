from django.db import models
from accounts.models import Customer


class Subscription(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name


class CustomerSubscription(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)