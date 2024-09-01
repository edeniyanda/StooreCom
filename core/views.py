from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Product, Order, ShippingAddress, OrderItem, Customer

def home(request):
    products = Product.objects.all()

    return render(request, "core/home.html", { "products" : products})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {
            "total_items" : 0,
            "total_price" : 0
        }

    context = {
        "items": items, 
        "order" : order
    }

    return render(request, "core/cart.html", context)

def check_out(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            "total_items" : 0,
            "total_price" : 0
        }

    context = {
        "items": items, 
        "order" : order
    }
    return render(request, "core/check_out.html", context)

