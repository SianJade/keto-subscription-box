from django.shortcuts import render

def index(request):
    """
    Return index.html page
    """
    return render(request, 'index.html')