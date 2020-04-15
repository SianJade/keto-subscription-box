from django.shortcuts import render


def index(request):
    """
    Display the index page
    """
    return render(request, 'index.html')
    