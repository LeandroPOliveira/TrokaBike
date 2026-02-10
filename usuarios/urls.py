from django.urls import path
from usuarios.views import (
    login_usuario,
    cadastro,
    logout_usuario,
    perfil,
    nova_senha
)

urlpatterns = [
    path('login', login_usuario, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('perfil', perfil, name='perfil'),
    path('nova-senha', nova_senha, name='nova_senha'),
    path('logout', logout_usuario, name='logout'),
]
