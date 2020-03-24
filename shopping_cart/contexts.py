from django.shortcuts import get_object_or_404
from all_products.models import Product

def cart_contents(request):
    """
    Ensures cart contents are available when rendering every page across the site
    """
    cart = request.session.get('cart', {})
    cart_items = []
    """
    Initialize cart total and product count
    """
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        """
        Total is a running cost of product price multiplied by product quantity
        """
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    """
    Return a dictionary of key value pairs for cart items, total, and product count
    """
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }