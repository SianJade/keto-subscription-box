from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

def index(request):
    """
    Return index.html page
    """
    return render(request, 'index.html')


def logout(request):
    """
    Log user out
    """
    auth.logout(request)
    messages.success(request, "Logout successful")
    return redirect(reverse('index'))


def login(request):
    """
    Return login page
    """
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(email=request.POST['email'],
                                     password=request.POST['password'])
            messages.success(request,"Login successful")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})