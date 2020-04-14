from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

# Create your tests here.
class TestAccountsAppForms(TestCase):
   def test_user_login_form(self):
        form = UserLoginForm({
            'username': 'name',
            'password': 'a_password'
        })
        self.assertTrue(form.is_valid())