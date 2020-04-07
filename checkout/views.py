from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import Order
from .models import OrderLineItem, SubscriptionOrderLineItem
from django.conf import settings
from django.utils import timezone
from all_products.models import Product
from subscribe.models import Subscription
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        """
        Provides the user with the order and payment forms to fill out
        """
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            """
            If the order and payment forms are both valid then save the order
            details, including the time and date the order was placed
            """
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
                
            """
            Retrieve information about which items have been purchased from 
            the user's current shopping cart in the session by using a for loop
            to iterate over the id and quantity of each cart item
            """
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                subscription = get_object_or_404(Subscription, pk=id)
                total += quantity * product.price
                total += quantity * subscription.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                subscription_line_item = SubscriptionOrderLineItem(
                    order = order,
                    subscription = subscription,
                    quantity = quantity
                    )
                order_line_item.save()
                subscription_line_item.save()
            
                
            try:
                """
                Create a customer charge using Stripe's built in API which must be
                multiplied by 100 as Stripe records everything in pence
                """
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card= payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                """
                Throw an error if the card is declined
                """
                messages.error(request, "Payment method declined")
                

            if customer.paid:
                """
                Inform the customer if their payment has been successful and 
                redirect them to the all products page
                """
                messages.error(request, "Payment successful")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to process payment")
        else:
            print(payment_form.errors)
            messages.error(request, "Unable to take payment from provided card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})