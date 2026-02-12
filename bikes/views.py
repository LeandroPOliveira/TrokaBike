from django.shortcuts import render, redirect, get_object_or_404
from bikes.models import Produto
from django.contrib import messages
from bikes.forms import ProdutoForm
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    produto = Produto.objects.order_by('-id').filter(publicada=True)
    titulo = 'Trokabike'
    ano = datetime.date.today().year
    return render(request, 'bikes/index.html', {'cards': produto, 'titulo': titulo, 'ano': ano})


@login_required
def criar_produto(request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuarios = request.user   # ⭐ dono do produto
            produto.save()

            messages.success(request, "Produto criado com sucesso!")
            return redirect('index')

    else:
        form = ProdutoForm()

    return render(request, 'bikes/criar_produto.html', {'form': form})


@login_required
def editar_produto(request, id):

    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)

        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect('detalhes_produto', id=produto.id)

    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'bikes/editar_produto.html', {'form': form})



def filtro(request, categoria):
    produto = Produto.objects.order_by('atualizado_em').filter(publicada=True, categoria=categoria)
    return render(request, 'bikes/index.html', {'cards': produto})


def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'bikes/detalhes_bike.html', {'produto': produto})


from django.contrib.auth.decorators import login_required

@login_required
def meus_produtos(request):
    produtos = Produto.objects.filter(usuario=request.user)

    return render(
        request,
        'bikes/meus_produtos.html',
        {'produtos': produtos}
    )
