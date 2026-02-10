from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForm, PerfilForm, NovaSenhaForm, UserInfoForm
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from payment.forms import EnderecoForm
from payment.models import Endereco
import json
from cart.cart import Cart


def login_usuario(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)

                usuario_atual = Profile.objects.get(usuario__id=request.user.id)

                cart_salvo = usuario_atual.old_cart
                if cart_salvo:
                    cart_convertido = json.loads(cart_salvo)
                    cart = Cart(request)

                    for key, value in cart_convertido.items():
                        cart.db_add(product=key, quantity=value)

                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar o login')
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})


from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.contrib.auth import authenticate, login


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CadastroForm


def cadastro(request):

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():

            # salva usuário
            user = form.save()

            # autentica
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(
                request,
                username=username,
                password=password
            )

            # login automático
            login(request, user)

            messages.success(request, 'Conta criada e login realizado!')
            return redirect('index')  # ajuste rota

    else:
        form = CadastroForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


@login_required
def perfil(request):
    if request.user.is_authenticated:

        current_user = request.user
        current_profile = Profile.objects.get(usuario=request.user)

        user_form = PerfilForm(request.POST or None, instance=current_user)
        perfil_form = UserInfoForm(request.POST or None, instance=current_profile)

        if request.method == 'POST':
            if user_form.is_valid() and perfil_form.is_valid():
                user_form.save()
                perfil_form.save()

                messages.success(request, "Perfil atualizado!")
                return redirect('perfil')

        return render(request, "usuarios/perfil.html", {
            'user_form': user_form,
            'perfil_form': perfil_form
        })

    messages.warning(request, "Faça login para acessar o perfil")
    return redirect('index')




from django.contrib.auth import update_session_auth_hash

def nova_senha(request):
    if request.user.is_authenticated:

        current_user = request.user

        if request.method == 'POST':
            form = NovaSenhaForm(current_user, request.POST)

            if form.is_valid():
                form.save()

                # ⭐ mantém sessão válida
                update_session_auth_hash(request, current_user)

                messages.success(request, "Your password has been updated!")
                return redirect('perfil')

            else:
                for error in form.errors.values():
                    messages.error(request, error)

        else:
            form = NovaSenhaForm(current_user)

        return render(request, "usuarios/nova-senha.html", {'form': form})

    else:
        messages.success(request, "You must be logged in.")
        return redirect('index')



def logout_usuario(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
