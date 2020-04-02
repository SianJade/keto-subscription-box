from django.shortcuts import get_object_or_404
from all_products.models import Product
from subscribe.models import Subscription

def cart_contents(request):
    """
    Ensures cart contents are available when rendering every page across the site
    """
    cart = request.session.get('cart', { 'product': {}, 'subscription': {}})
    print(cart)
    # cart = { 'product': {1 : 1}, 'subscription': {2 : 1}}
    cart_items = []
    print(bool(cart['product']))
    print(bool(cart['subscription']))
    """
    Initialize cart total and product count
    """
    total = 0
    product_count = 0
    if bool(cart['product']):
        print(type(cart['product']))
        for product_id, quantity in cart['product']:
            product = get_object_or_404(Product, pk=product_id)
            total += product.price * quantity
            product_count += quantity
            cart_items.append({'product_id': product_id, 'quantity': quantity})

    if bool(cart['subscription']):
        for subscription_id, quantity in cart['subscription']:
            subscription = get_object_or_404(Subscription, pk=subscription_id)
            total += subscription.price * quantity
            product_count += quantity
            cart_items.append({'subscription_id': subscription_id, 'quantity': quantity})

    """
    Return a dictionary of key value pairs for cart items, total, and product count
    """
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }