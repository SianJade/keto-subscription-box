from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


class TestUserLoginForm(TestCase):
    def test_user_login_form(self):
        form = UserLoginForm({
            'username': 'name',
            'password': 'a_password'
        })
        self.assertTrue(form.is_valid())


class TestUserRegistrationForm(TestCase):
    def test_user_registration_form_is_valid(self):
        form = UserRegistrationForm({
            'first_name': 'Mrs',
            'last_name': 'Smith',
            'email': 'testemail@gmail.com',
            'username': 'NewUser',
            'password1': 'hereisapassword',
            'password2': 'hereisapassword'
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_if_invalid_email(self):
        form = UserRegistrationForm({
            'first_name': 'Mrs',
            'last_name': 'Smith',
            'email': 'this is not an email address',
            'username': 'NewUser',
            'password1': 'hereisapassword',
            'password2': 'hereisapassword'
        })
        self.assertFalse(form.is_valid())
        print(form.errors['email'], ['Please enter a valid email address'])

    def test_registration_form_invalid_passwords_do_not_match(self):
        form = UserRegistrationForm({
            'first_name': 'Mrs',
            'last_name': 'Smith',
            'email': 'testemail@gmail.com',
            'username': 'NewUser',
            'password1': 'hereisapassword',
            'password2': 'notthesamepassword'
        })
        self.assertFalse(form.is_valid())

    def test_user_registration_form_returns_invalid_if_no_username_input(self):
        form = UserRegistrationForm({
            'first_name': 'Mrs',
            'last_name': 'Smith',
            'email': 'testemail@gmail.com',
            'username': '',
            'password1': 'hereisapassword',
            'password2': 'hereisapassword'
        })
        self.assertFalse(form.is_valid())
        print(form.errors['username'], ['Please enter a username'])
