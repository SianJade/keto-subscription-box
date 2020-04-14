from django.test import TestCase
from .models import Subscription


class TestSubscriptionCreation(TestCase):
    def test_subscription_creation(self):
        # assertions are listed in the order in which the fields appear in the Subscription model
        subscription = Subscription(name='1 Month',
                        price='35.00')
        self.assertEqual(subscription.name, '1 Month')
        self.assertFalse(subscription.duration)
        self.assertFalse(subscription.description)
        self.assertNotEqual(subscription.price, '25.00')
        self.assertFalse(subscription.image)