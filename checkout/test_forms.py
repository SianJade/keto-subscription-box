from django.test import TestCase
from .forms import MakePaymentForm, OrderForm


class TestMakePaymentForm(TestCase):
    def test_payment_form(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': '',
            'expiry_month': '3',
            'expiry_year': '2022'
        })
        self.assertFalse(form.is_valid())


class TestOrderForm(TestCase):
    def test_order_form_is_valid(self):
        form = OrderForm({'full_name': 'Jane Doe',
                          'street_address1': 'street name',
                          'street_address2': 'street name 2',
                          'town_or_city': 'Manchester',
                          'county': 'Lancashire',
                          'postcode': 'OL9 0QG',
                          'country': 'England',
                          'phone_number': '123456789'
                          })
        self.assertTrue(form.is_valid())

    def test_order_form_can_still_be_valid_with_no_address_line2(self):
        form = OrderForm({'full_name': 'Jane Doe',
                          'street_address1': 'street name',
                          'street_address2': '',
                          'town_or_city': 'Manchester',
                          'county': 'Lancashire',
                          'postcode': 'OL9 0QG',
                          'country': 'England',
                          'phone_number': '123456789'
                          })
        self.assertTrue(form.is_valid())

    def test_order_form_can_still_be_valid_with_no_county(self):
        form = OrderForm({'full_name': 'Jane Doe',
                          'street_address1': 'street name',
                          'street_address2': 'street name 2',
                          'town_or_city': 'Manchester',
                          'county': '',
                          'postcode': 'OL9 0QG',
                          'country': 'England',
                          'phone_number': '123456789'
                          })
        self.assertTrue(form.is_valid())

    def test_order_form_is_not_valid_without_postcode(self):
        form = OrderForm({'full_name': 'Jane Doe',
                          'street_address1': 'street name',
                          'street_address2': 'street name 2',
                          'town_or_city': 'Manchester',
                          'county': 'Lancashire',
                          'postcode': '',
                          'country': 'England',
                          'phone_number': '123456789'
                          })
        self.assertFalse(form.is_valid())

    def test_order_form_is_not_valid_without_name(self):
        form = OrderForm({'full_name': '',
                          'street_address1': 'street name',
                          'street_address2': 'street name 2',
                          'town_or_city': 'Manchester',
                          'county': 'Lancashire',
                          'postcode': 'OL9 0QG',
                          'country': 'England',
                          'phone_number': '123456789'
                          })
        self.assertFalse(form.is_valid())

    def test_order_form_is_not_valid_without_town_or_city(self):
        form = OrderForm({'full_name': 'Jane Doe',
                          'street_address1': 'street name',
                          'street_address2': 'street name 2',
                          'town_or_city': '',
                          'county': 'Lancashire',
                          'postcode': 'OL9 0QG',
                          'country': 'England',
                          'phone_number': '123456789'
                          })
        self.assertFalse(form.is_valid())
