from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()

    return render(request, "core/home.html", { "products" : products})

def cart(request):
    return render(request, "core/cart.html", {})

def check_out(request):
    return render(request, "core/check_out.html", {})

