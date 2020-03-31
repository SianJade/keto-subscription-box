from django.conf.urls import url, include
from .views import all_subs
from shopping_cart.views import add_to_cart

urlpatterns = [
    url(r'^$', all_subs, name='subscriptions'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
]