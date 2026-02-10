from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    class Meta:
        verbose_name_plural = 'Perfil'

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_modificacao = models.DateTimeField(auto_now=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=200, blank=True)
    cep = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(usuario=instance)




