from django.db import models
from all_products.models import Product
from subscribe.models import Subscription


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}".format(self.full_name, self.date)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} @ {1}".format(self.product.name, self.quantity)


class SubscriptionOrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.CASCADE,
                                     null=True)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} @ {1}".format(self.subscription.name, self.quantity)
