from django.conf.urls import url, include
from .views import all_products, view_product
from shopping_cart.views import add_to_cart

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^product/(?P<pk>\d+)/$', view_product, name='view_product')
]