from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

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