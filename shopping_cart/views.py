from django.shortcuts import render, redirect, reverse
from all_products.models import Product
from subscribe.models import Subscription


def view_cart(request):
    return render(request, 'cart.html')


def add_to_cart(request, id, category):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {'product': {},
                                        'subscription': {}})

    if id in cart[category]:
        cart[category][id] = int(cart[category][id]) + quantity
    else:
        cart[category][id] = quantity

    request.session['cart'] = cart
    if category == 'product':
        return redirect(reverse('products'))
    else:
        return redirect(reverse('subscriptions'))


def adjust_cart(request, id, category):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {'product': {},
                                        'subscription': {}})

    if quantity > 0:
        cart[category][id] = quantity
    else:
        cart[category].pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
