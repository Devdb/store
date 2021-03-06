from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from market.models import Product, Cart, Employee, ProductInCart
from market.forms import RegisterForm, LoginForm


def home(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        return render(request, 'home.html', context={'employees': employees})

    return HttpResponse(status=405)


def products_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return render(request, 'login_failed.html')
        cart, _ = Cart.objects.get_or_create(client=request.user)
        products_in_cart = []
        for key in request.POST.keys():
            if key.startswith('product_id__'):
                product_id = int(key.split('product_id__')[1])
                count = request.POST[f'count__{product_id}']
                product_in_cart = ProductInCart.objects.create(product=Product.objects.get(id=product_id), count=count)
                products_in_cart.append(product_in_cart)
        cart.products.add(*products_in_cart)
        cart.calc_sum()
        cart.save()
        return redirect('cart', permanent=True)
    if request.method == 'GET':
        product_list = Product.objects.all()
        return render(request, 'products.html', context={'list': product_list})

    return HttpResponse(status=405)


def cart_view(request):
    if not request.user.is_authenticated:
        return render(request, 'login_failed.html')

    if request.is_ajax() and request.method == 'POST':
        try:
            product_to_delete = request.POST.getlist('deleted[]')
            cart = Cart.objects.get(client=request.user)
            for product_id in product_to_delete:
                product_obj = ProductInCart.objects.get(id=product_id)
                cart.products.remove(product_obj)
            cart.calc_sum()
            cart.save()

            # Calculating context
            try:
                cart = Cart.objects.get(client=request.user)
                products_in_cart = cart.products.all()
                overall_sum = cart.overall_sum
            except Cart.DoesNotExist:
                products_in_cart = []
                overall_sum = 0
            context = {'products_list': products_in_cart, 'overall_sum': overall_sum}
            return HttpResponse(render(request, 'forms/cart_form.html', context=context), status=200)
        except Exception as e:
            return HttpResponse(e.__str__(), status=500)

    if request.method == 'GET':
        try:
            cart = Cart.objects.get(client=request.user)
            products_in_cart = cart.products.all()
            overall_sum = cart.overall_sum
        except Cart.DoesNotExist:
            products_in_cart = []
            overall_sum = 0
        context = {'products_list': products_in_cart, 'overall_sum': overall_sum}
        return render(request, 'cart.html', context=context)
    else:
        return HttpResponse(status=405)


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
