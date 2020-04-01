from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """
    Display all cart contents
    """
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """
    Add selected item to cart
    """
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    if id in cart:
        """
        If the id of the selected product is already in the user's shopping cart
        and they wish to add another of the same item, then get the integer that
        is the product quantity and add the new product quantity to it
        """
        cart[id] = int(cart[id]) + quantity
    else:
        """
        If the item with the selected id is not already in the user's cart, then
        add the specified quantity of the selected item to the user's cart
        """
        cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the chosen product to the desired amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))