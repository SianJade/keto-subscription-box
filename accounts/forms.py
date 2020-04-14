from django import forms
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    """
    Form used for user login
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """
    Form to register a new user
    """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation",
                                widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            """
            if a user with the entered email already exists in the 
            database, return an error
            """
            raise forms.ValidationError(u'A user  with this email address already exists')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            """
            Check to see if both passwrd fields have been filled out by the user
            """
            raise ValidationError(u'Please confirm your password')
        
        if password1 != password2:
            """
            If password1 doesn't match password 2 return an error
            """
            raise ValidationError(u'Passwords must match')
        
        return password2