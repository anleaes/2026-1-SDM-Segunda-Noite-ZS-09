from django.db import models
from django.utils import timezone

from apps.cliente.models import Cliente


class CarteiraMotorista(models.Model):
    numeroRegistro = models.CharField(max_length=20, unique=True)
    categoria = models.CharField(max_length=5)
    dataValidade = models.DateField()
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='carteiraMotorista')

    def isValida(self):
        return self.dataValidade >= timezone.now().date()

    def __str__(self):
        return f"CNH {self.numeroRegistro} ({self.categoria})"
