from django import forms
from bikes.models import Produto
from datetime import datetime


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        exclude = ['publicada', 'usuarios']
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',

        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'cor': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'categoria': forms.Select(attrs={'class': 'form-control mb-3'}),
            'preco': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'ano': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'foto': forms.FileInput(attrs={'type': "file", 'class': "form-control-file mt-3", 'id': "foto", 'name': "foto",
            'accept': "image/*", 'onchange': "previewImage(this)"}),
            'data_fotografia': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'value': datetime.now().strftime("%d/%m/%Y")}),
            'usuarios': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'