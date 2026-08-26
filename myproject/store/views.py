from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def products(request):
    return render(request, 'product.html')


def cart(request):
    return render(request, 'cart.html')