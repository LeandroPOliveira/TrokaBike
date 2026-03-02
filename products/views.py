from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

from .models import Product
from .forms import ProductForm


def product_list(request):
    search = request.GET.get("q")

    products = Product.objects.filter(is_published=True)

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    products = products.order_by("-created_at")

    paginator = Paginator(products, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "products/product_list.html",
        {
            "page_obj": page_obj,
            "search": search,
            "year": timezone.now().year,
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_published=True)

    return render(
        request,
        "products/product_detail.html",
        {"product": product},
    )


@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.is_published = True
            product.save()

            messages.success(request, "Product created successfully!")
            return redirect(product.get_absolute_url())
    else:
        form = ProductForm()

    return render(request, "products/product_form.html", {"form": form})


@login_required
def product_update(request, slug):
    product = get_object_or_404(Product, slug=slug, user=request.user)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect(product.get_absolute_url())
    else:
        form = ProductForm(instance=product)

    return render(request, "products/product_form.html", {"form": form})


@login_required
def product_delete(request, slug):
    product = get_object_or_404(Product, slug=slug, user=request.user)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect("products:my_products")

    return render(
        request,
        "products/product_confirm_delete.html",
        {"product": product},
    )


@login_required
def my_products(request):
    search = request.GET.get("q")

    products = Product.objects.filter(user=request.user)

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    products = products.order_by("-created_at")

    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "products/my_products.html",
        {
            "page_obj": page_obj,
            "search": search,
        },
    )


def product_by_category(request, category):
    products = Product.objects.filter(
        is_published=True,
        category__iexact=category
    ).order_by("-created_at")

    return render(
        request,
        "products/product_list.html",
        {"page_obj": products},
    )