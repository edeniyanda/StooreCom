from django.contrib import admin
from .models import *



admin.site.register([Customer, Product, Order, OrderItem, ShippingAddress])
