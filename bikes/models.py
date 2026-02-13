from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid


class Produto(models.Model):

    class Meta:
        verbose_name_plural = "Produtos"

    OPCOES_CATEGORIA = [
        ('MOUNTAIN', "Mountain"),
        ('ROAD', 'Road'),
        ('GRAVEL', 'Gravel'),
        ('VESTUARIO', 'Vestuario')
    ]

    nome = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)

    categoria = models.CharField(
        max_length=100,
        choices=OPCOES_CATEGORIA,
        default='MOUNTAIN'
    )

    cor = models.CharField(max_length=40)
    preco = models.DecimalField(max_digits=9, decimal_places=2)

    ano = models.PositiveIntegerField()

    descricao = models.TextField()

    foto = models.ImageField(
        upload_to="fotos/%Y/%m/%d",
        blank=True
    )

    publicada = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="produtos"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nome)
            unique_slug = base_slug

            while Produto.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{uuid.uuid4().hex[:5]}"

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
