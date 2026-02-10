# 🚲 TrokaBike — Django E-Commerce Platform

TrokaBike é um projeto de e-commerce desenvolvido com Django com o objetivo de simular uma aplicação real de marketplace para compra e venda de bicicletas e acessórios.

O projeto foi criado para estudo e evolução em desenvolvimento backend/full-stack com Python, focando em arquitetura web, autenticação, carrinho de compras e fluxo de pagamento.

---

## 🌐 Demo



🔗 Live:  
🔗 Admin:  

---

## 🧰 Stack Tecnológica

### Backend
- Python
- Django
- SQLite (dev)

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Outros
- Django ORM
- Templates Django
- Static/Media handling

---

## 📦 Funcionalidades Implementadas

- Cadastro e autenticação de usuários
- Listagem de produtos
- Página de detalhe do produto
- Carrinho de compras
- Fluxo básico de pagamento
- Upload de imagens
- Interface administrativa via Django Admin

---

## 🏗 Arquitetura do Projeto

O projeto segue estrutura modular baseada em apps Django:

bikes/ → catálogo de produtos
cart/ → carrinho de compras
payment/ → fluxo de pagamento
usuarios/ → autenticação e usuários
setup/ → configurações do projeto


Separação por domínio facilita escalabilidade e manutenção.

---

## 🚀 Como executar o projeto




1️⃣ Clonar repositório
git clone https://github.com/LeandroPOliveira/TrokaBike.git


2️⃣Criar ambiente virtual
python -m venv venv
source venv/bin/activate


Windows:

venv\Scripts\activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Rodar migrations
python manage.py migrate

5️⃣ Executar servidor
python manage.py runserver


## 🎯 Objetivo do Projeto

Este projeto faz parte do meu portfólio para transição e crescimento na área de desenvolvimento Python, demonstrando:

Arquitetura Django

Modelagem de dados

Desenvolvimento full-stack

Boas práticas de organização de código
