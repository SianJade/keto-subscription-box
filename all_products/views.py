from django.shortcuts import render, get_object_or_404
from .models import Product, Ingredients, ProductIngredients, NutritionValue

def all_products(request):
    """
    Shows the user all products available for purchase on one page
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products":  products})


def view_product(request, id):
    """
    View more detailed information about a single product on its own page
    """
    product = get_object_or_404(Product, id=id)
    nutrition = get_object_or_404(NutritionValue, id=id)
    ingredients = product.ingredients.all()
    return render(request, "product.html", {"product": product, "nutrition": nutrition, 'ingredients': ingredients})

    