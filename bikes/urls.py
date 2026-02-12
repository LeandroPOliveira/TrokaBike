from django.urls import path
# from bikes.views import index, nova_bike, editar_bike, filtro, detalhes_bike
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('novo-produto/', views.criar_produto, name='criar_produto'),
    path('editar-produto/<int:id>', views.editar_produto, name='editar_produto'),
    path('meus-produtos/', views.meus_produtos, name='meus_produtos'),
    path('detalhes-bike/<int:id>', views.detalhes_produto, name='detalhes_produto'),
    path('filtro/<str:categoria>', views.filtro, name='filtro'),

]

