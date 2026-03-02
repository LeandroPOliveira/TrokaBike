import json

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import (
    LoginForm,
    RegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    PasswordChangeCustomForm,
)

from .models import Profile
from cart.cart import Cart


# -----------------------------
# Login
# -----------------------------

def login_user(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)

                # Restore saved cart
                profile, _ = Profile.objects.get_or_create(user=user)

                if profile.saved_cart:
                    cart_data = json.loads(profile.saved_cart)
                    cart = Cart(request)

                    for product_id, quantity in cart_data.items():
                        cart.db_add(product=product_id, quantity=quantity)

                messages.success(request, "Login successful!")
                return redirect("products:my_products")

            messages.error(request, "Invalid credentials.")

    return render(request, "users/login.html", {"form": form})


# -----------------------------
# Register
# -----------------------------

def register_user(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Auto login
            raw_password = form.cleaned_data["password1"]
            user = authenticate(
                request,
                username=user.username,
                password=raw_password,
            )

            login(request, user)

            messages.success(request, "Account created successfully!")
            return redirect("products:product_list")

    return render(request, "users/register.html", {"form": form})


# -----------------------------
# Profile
# -----------------------------

@login_required
def profile_user(request):

    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":

        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Profile updated successfully!")
            return redirect("users:profile")

    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(
        request,
        "users/profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )

# -----------------------------
# Change Password
# -----------------------------

@login_required
def change_password_user(request):
    if request.method == "POST":
        form = PasswordChangeCustomForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)

            messages.success(request, "Password updated successfully!")
            return redirect("users:profile")
    else:
        form = PasswordChangeCustomForm(request.user)

    return render(request, "users/change_password.html", {"form": form})


# -----------------------------
# Logout
# -----------------------------

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("users:login")