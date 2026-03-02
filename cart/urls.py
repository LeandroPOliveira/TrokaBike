from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/', views.cart_add, name="cart_add"),
    path('cart-remove/', views.cart_remove, name='cart_remove'),
    path('cart-update/', views.cart_update, name='cart_update'),
]

