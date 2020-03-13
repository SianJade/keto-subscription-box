from django.shortcuts import render

def login(request):
    """
    Return login.html page
    """
    return render(request, 'login.html')