from django.urls import path
from .views import (
    login_user,
    register_user,
    logout_user,
    profile_user,
    change_password_user,
)

app_name = "users"

urlpatterns = [
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("profile/", profile_user, name="profile"),
    path("change-password/", change_password_user, name="change_password"),
    path("logout/", logout_user, name="logout"),
]