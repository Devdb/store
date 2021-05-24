from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from market.models import Product, Cart, Employee
from market.forms import RegisterForm, LoginForm


def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', context={'employees': employees})


def products_view(request):
    if request.method == 'POST':
        cart, _ = Cart.objects.get_or_create(client=request.user)
        product_in_cart = []
        for key in request.POST.keys():
            if key.startswith('product_id__'):
                product_id = int(key.split('product_id__')[1])
                product_in_cart.append(Product.objects.get(id=product_id))
        cart.products.clear()
        cart.products.add(*product_in_cart)
        cart.calc_sum()
        cart.save()
        return redirect('cart', permanent=True)

    product_list = Product.objects.all()
    return render(request, 'products.html', context={'list': product_list})


def cart_view(request):
    if not request.user.is_authenticated:
        return render(request, 'login_failed.html')
    if request.is_ajax():
        print('dsasddsa')
    if request.method == 'POST':
        cart = Cart.objects.get(client=request.user)
        for key in request.POST.keys():
            if key.startswith('product_id__'):
                product_id = int(key.split('product_id__')[1])
                product_obj = Product.objects.get(id=product_id)
                cart.products.remove(product_obj)
        cart.calc_sum()
        cart.save()
        return redirect('cart', permanent=True)

    else:
        try:
            cart = Cart.objects.get(client=request.user)
            products_in_cart = cart.products.all()
            overall_sum = cart.overall_sum
        except Cart.DoesNotExist:
            products_in_cart = []
            overall_sum = 0
        context = {'products_list': products_in_cart, 'overall_sum': overall_sum}
        return render(request, 'cart.html', context=context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home', permanent=True)
        return render(request, 'login_failed.html', status=403)
    login_form = LoginForm()
    return render(request, 'login.html', context={'form': login_form})


def logout_view(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
    return redirect('home', permanent=True)


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('home', permanent=True)
    register_form = RegisterForm()
    return render(request, 'register.html', context={'form': register_form})
