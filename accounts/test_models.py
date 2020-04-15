from django.test import TestCase
from .models import User, Customer


class TestUserCreation(TestCase):
    def test_user_creation(self):
        """
        Assertions are listed in the order in which
        the fields appear in the User model
        """
        user = User(username='User',
                    password='thisisapassword',
                    email='testemail@gmail.com')
        self.assertEqual(user.username, 'User')
        self.assertNotEqual(user.username, 'incorrectpassword')
        self.assertFalse(user.first_name)
        self.assertFalse(user.last_name)
        self.assertEqual(user.email, 'testemail@gmail.com')


class TestCustomerCreation(TestCase):
    def test_customer_creation(self):
        customer = Customer(dietary_preference='pescetarian',
                            allegeries_intolerances='wheat')
        self.assertEqual(customer.dietary_preference, 'pescetarian')
        self.assertNotEqual(customer.dietary_preference, 'vegan')
        self.assertEqual(customer.allegeries_intolerances, 'wheat')
        self.assertNotEqual(customer.allegeries_intolerances, 'none')
