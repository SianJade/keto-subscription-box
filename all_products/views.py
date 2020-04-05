from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":  products})

def view_product(request, id):
    products = Product.objects.all()
    product = Product, id
    return render(request, "product.html", {"product": product})