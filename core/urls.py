from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,  name="home_page"),
    path('cart/', views.cart,  name="cart_page"),
    path('chectout/', views.check_out,  name="check_out_page"),
]
