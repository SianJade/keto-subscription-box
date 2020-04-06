from django.db import models
from all_products.models import Product
from subscribe.models import Subscription
from accounts.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_timestamp = models.DateTimeField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.total, self.customer.name)


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