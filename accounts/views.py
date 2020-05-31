from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Customer
from .forms import CustomerForm
from accounts.forms import UserLoginForm, UserRegistrationForm


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout successful")
    return redirect(reverse('index'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Login successful")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Incorrect username or password")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """
    Render registration page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if registration_form.is_valid() and customer_form.is_valid():
            user = registration_form.save()
            Customer = customer_form.save(commit=False)
            Customer.user = user
            Customer.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'Account registration successful')
                return render(request, 'index.html')
            else:
                messages.error(
                    request,
                    'Unable to register your account at this time'
                )
    else:
        registration_form = UserRegistrationForm()
        customer_form = CustomerForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form,
        "customer_form": customer_form
        })


def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
