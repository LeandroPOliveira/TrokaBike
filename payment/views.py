from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from payment.forms import AddressForm
from payment.models import Order, OrderItem


def checkout(request):
    cart = Cart(request)

    cart_items = cart.get_cart_items()
    total = cart.get_total_price()

    if not cart_items:
        messages.warning(request, "Your cart is empty.")
        return redirect("cart_detail")

    if request.method == "POST":
        form = AddressForm(request.POST)

        if form.is_valid():

            address = form.save(commit=False)

            if request.user.is_authenticated:
                address.user = request.user

            address.save()

            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                address=address,
                total_amount=total,
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    user=request.user if request.user.is_authenticated else None,
                    quantity=item["quantity"],
                    price=item["product"].price,
                )

            cart.clear()

            messages.success(request, "Order placed successfully!")

            return redirect("payment_success")
    else:
        form = AddressForm()

    return render(
        request,
        "payment/checkout.html",
        {
            "cart_items": cart_items,
            "total": total,
            "form": form,
        },
    )



def payment_success(request):
    return render(request, "payment/payment_success.html")

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "payment/my_orders.html", {
        "orders": orders
    })