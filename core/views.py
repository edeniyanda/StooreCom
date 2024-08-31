from django.shortcuts import render

def home(request):
    return render(request, "core/home.html", {})

def cart(request):
    return render(request, "core/cart.html", {})

def check_out(request):
    return render(request, "core/check_out.html", {})

