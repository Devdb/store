from django.urls import path
from market.views import home, products, cart

urlpatterns = [
    path('', home, name='home'),
    path('products', products, name='products'),
    path('cart', cart, name='cart')
]
