from django.test import TestCase
from .models import Order

class TestOrderCreation(TestCase):
    def test_order_creation(self):
        # assertions are listed in the order in which the fields appear in the Order model
        order = Order(full_name='Mrs Name',
                        county='Lancashire',
                        postcode='NE66 1QF',
                        phone_number='123456789')
        self.assertEqual(order.full_name, 'Mrs Name')
        self.assertFalse(order.street_address1)
        self.assertFalse(order.street_address2)
        self.assertFalse(order.town_or_city)
        self.assertNotEqual(order.county, 'Northumberland')
        self.assertNotEqual(order.postcode, 'OL9 0QG')
        self.assertFalse(order.country)
        self.assertEqual(order.phone_number, '123456789')