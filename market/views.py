from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from market.models import Product
from django.contrib.auth import authenticate


def home(request):
    return render(request, 'home.html')


def products(request):
    product_list = Product.objects.all()
    return render(request, 'products.html', context=product_list)


def cart(request):
    if not request.user.is_authenticated:
        return render(request, 'login_failed.html')
    print('just')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        return redirect('home', permanent=True)
    else:
        return render(request, 'login_failed.html', status=403)


def register_view(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.save()
    return redirect('home', permanent=True)
