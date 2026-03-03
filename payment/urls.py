from django.urls import path
from . import views

urlpatterns = [
    path('payment-success/', views.payment_success, name='payment_success'),
    path('checkout', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders'),
]
