from django.shortcuts import render, get_object_or_404
from .models import Product, Ingredients, ProductIngredients, NutritionValue


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":  products})


def view_product(request, id):
    product = get_object_or_404(Product, id=id)
    nutrition = get_object_or_404(NutritionValue, id=id)
    ingredients = product.ingredients.all()
    return render(request, "product.html", {
        "product": product,
        "nutrition": nutrition,
        'ingredients': ingredients
        })
