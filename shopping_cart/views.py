from django.shortcuts import render

def view_cart(request):
    """
    Display all cart contents
    """
    return render(request, 'cart.html')