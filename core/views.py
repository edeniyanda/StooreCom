from django.shortcuts import render

def home(request):
    return render(request, "core/home.html", {})

def cart(request):
    return render(request, "core/cart.html", {})

