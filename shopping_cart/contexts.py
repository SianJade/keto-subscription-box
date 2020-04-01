from django.shortcuts import get_object_or_404
from all_products.models import Product
from subscribe.models import Subscription

def cart_contents(request):
    """
    Ensures cart contents are available when rendering every page across the site
    """
    cart = request.session.get('cart', { 'product': {}, 'subscription': {}})
    cart_items = []
    """
    Initialize cart total and product count
    """
    total = 0
    product_count = 0
    for product_id, quantity in cart['product']:
        product = get_object_or_404(Product, pk=product_id)
        total += product.price * quantity
        product_count += quantity
        cart_items.append({'product_id': product_id, 'quantity': quantity})

    for subscription_id, quantity in cart['subscription']:
        subscription = get_object_or_404(Subscription, pk=subscription_id)
        total += subscription.price * quantity
        product_count += quantity
        cart_items.append({'subscription_id': subscription_id, 'quantity': quantity})

    """
    Return a dictionary of key value pairs for cart items, total, and product count
    """
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }