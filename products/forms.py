from django import forms
from .models import Product
from datetime import datetime


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = [
            "slug",
            "user",
            "is_published",
            "created_at",
            "updated_at",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control mb-3",
                "placeholder": "Product name"
            }),

            "category": forms.Select(attrs={
                "class": "form-control mb-3"
            }),

            "color": forms.TextInput(attrs={
                "class": "form-control mb-3",
                "placeholder": "Color"
            }),

            "price": forms.NumberInput(attrs={
                "class": "form-control mb-3",
                "step": "0.01",
                "placeholder": "Price"
            }),

            "year": forms.NumberInput(attrs={
                "class": "form-control mb-3",
                "placeholder": "Year"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control mb-3",
                "rows": 4,
                "placeholder": "Product description"
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control mb-3",
                "accept": "image/*"
            }),
        }

    # -----------------------------
    # Custom Validation Example
    # -----------------------------
    def clean_year(self):
        year = self.cleaned_data.get("year")
        current_year = datetime.now().year

        if year > current_year:
            raise forms.ValidationError("Year cannot be in the future.")

        if year < 1900:
            raise forms.ValidationError("Year seems invalid.")

        return year