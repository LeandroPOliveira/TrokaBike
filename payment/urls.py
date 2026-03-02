from django.urls import path
from . import views

urlpatterns = [
    path('pagamento-sucesso/', views.payment_success, name='pagamento_success'),
    path('checkout', views.checkout, name='checkout'),
    path('meus-pedidos/', views.my_orders, name='my_orders'),
]
