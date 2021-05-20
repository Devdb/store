from django.urls import path
from market.views import home, products_view, cart_view

urlpatterns = [
    path('', home, name='home'),
    path('products', products_view, name='products'),
    path('cart', cart_view, name='cart')
]
