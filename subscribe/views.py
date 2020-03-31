from django.shortcuts import render
from .models import Subscription

def all_subs(request):
    subscriptions = Subscription.objects.all()
    return render(request, "subscriptions.html", {"subscriptions":  subscriptions})