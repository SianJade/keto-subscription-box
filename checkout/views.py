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
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {'product': {},
                                                'subscription': {}})
            total = 0
            for category, category_items in cart.items():
                for id, quantity in category_items.items():
                    if category == "product":
                        product = get_object_or_404(Product, id=id)
                        total += quantity * product.price
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity
                            )
                        order_line_item.save()
                    if category == "subscription":
                        subscription = get_object_or_404(Subscription, id=id)
                        total += quantity * subscription.price
                        subscription_line_item = SubscriptionOrderLineItem(
                            order=order,
                            subscription=subscription,
                            quantity=quantity
                            )
                        subscription_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Payment method declined")

            if customer.paid:
                messages.error(request, "Payment successful")
                request.session['cart'] = {'product': {}, 'subscription': {}}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to process payment")
        else:
            print(payment_form.errors)
            messages.error(request,
                           "Unable to take payment from provided card"
                           )
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html",
                  {'order_form': order_form,
                   'payment_form': payment_form,
                   'publishable': settings.STRIPE_PUBLISHABLE
                   })
