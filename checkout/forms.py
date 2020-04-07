from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    """
    Allows the user to select the expiry month and year for their chosen card
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]
    
    """
    Fields for user to input their card details
    """
    credit_card_number = forms.CharField(label='Credit/debit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        """
        Allows user to input their delievery details
        """
        model = Order
        fields = (
            'full_name',  'street_address1', 'street_address2', 'town_or_city',
            'county',  'postcode', 'country', 'phone_number'
        )