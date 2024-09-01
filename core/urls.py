from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,  name="home_page"),
    path('cart/', views.cart,  name="cart_page"),
    path('chectout/', views.check_out,  name="check_out_page"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
