from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from accounts import urls as accounts_urls
from all_products import urls as products_urls
from all_products.views import all_products
from shopping_cart import urls as shopping_cart_urls
from search import urls as search_urls
from checkout import urls as checkout_urls
from subscribe import urls as subscription_urls
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^all_products/', include(products_urls)),
    url(r'^cart/', include(shopping_cart_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^subscribe/', include(subscription_urls)),
    url(r'^media/(?P<path>.*$)', static.serve, {'document_root': MEDIA_ROOT}),
]
