from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    SetPasswordForm,
)
from .models import Profile

User = get_user_model()


# -----------------------------
# Login Form
# -----------------------------
class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        })
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )


# -----------------------------
# Register Form
# -----------------------------
class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email"
        })
    )

    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First Name"
        })
    )

    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        })
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })
        self.fields["username"].label = ""

        for field in ["password1", "password2"]:
            self.fields[field].widget.attrs.update({
                "class": "form-control",
                "placeholder": "Password"
            })
            self.fields[field].label = ""


# -----------------------------
# Update User Basic Info
# -----------------------------
class UserUpdateForm(UserChangeForm):

    password = None  # Remove password field

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email"
        })
    )

    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First Name"
        })
    )

    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        })
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })
        self.fields["username"].label = ""


# -----------------------------
# Update Extra Profile Info
# -----------------------------
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            "phone",
            "address",
            "city",
            "postal_code",
            "avatar",
        )

        widgets = {
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone"
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Address"
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "City"
            }),
            "postal_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Postal Code"
            }),
        }


# -----------------------------
# Change Password Form
# -----------------------------
class PasswordChangeCustomForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["new_password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "New Password"
        })
        self.fields["new_password1"].label = ""

        self.fields["new_password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm Password"
        })
        self.fields["new_password2"].label = ""