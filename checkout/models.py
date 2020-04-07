from django.db import models
from all_products.models import Product
from subscribe.models import Subscription
from accounts.models import Customer


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=20, blank=False, default='')
    country = models.CharField(max_length=40, blank=False, default='')
    postcode = models.CharField(max_length=20, blank=True, default='')
    town_or_city = models.CharField(max_length=40, blank=False, default='')
    street_address1 = models.CharField(max_length=40, blank=False, default='')
    street_address2 = models.CharField(max_length=40, blank=False, default='')
    county = models.CharField(max_length=40, blank=False, default='')
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)



class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)

class SubscriptionOrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.subscription.name, self.subscription.price)