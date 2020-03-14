from django import forms

class UserLoginForm(forms.Form):
    """
    Form used for user login
    """
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)