from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages

from .cart import Cart
from products.models import Product


def cart_detail(request):
    """
    Display cart summary page.
    """
    cart = Cart(request)

    context = {
        "cart_items": cart.get_cart_items(),
        "totals": cart.get_total_price(),
    }

    return render(request, "cart/cart_detail.html", context)


@require_POST
def cart_add(request):
    """
    Add a product to the cart.
    """
    cart = Cart(request)

    try:
        product_id = int(request.POST.get("product_id"))
        quantity = int(request.POST.get("product_qty", 1))
    except (TypeError, ValueError):
        return JsonResponse({"error": "Invalid data"}, status=400)

    product = get_object_or_404(Product, id=product_id)

    cart.add(product=product, quantity=quantity)

    messages.success(request, "Product added to cart.")

    return JsonResponse({"qty": len(cart)})


@require_POST
def cart_remove(request):
    """
    Remove a product from the cart.
    """
    cart = Cart(request)

    try:
        product_id = int(request.POST.get("product_id"))
    except (TypeError, ValueError):
        return JsonResponse({"error": "Invalid data"}, status=400)

    cart.remove(product_id=product_id)

    messages.success(request, "Item removed from cart.")

    return JsonResponse({"product_id": product_id})


@require_POST
def cart_update(request):
    """
    Update product quantity in the cart.
    """
    cart = Cart(request)

    try:
        product_id = int(request.POST.get("product_id"))
        quantity = int(request.POST.get("product_qty"))
    except (TypeError, ValueError):
        return JsonResponse({"error": "Invalid data"}, status=400)

    cart.update(product_id=product_id, quantity=quantity)

    messages.success(request, "Cart updated successfully.")

    return JsonResponse({"qty": quantity})