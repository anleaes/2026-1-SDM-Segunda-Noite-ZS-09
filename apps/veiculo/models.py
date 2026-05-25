from django.db import models

from apps.agencia.models import Agencia
from apps.categoria_veiculo.models import CategoriaVeiculo


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=80)
    ano = models.PositiveIntegerField()
    valorDiaria = models.DecimalField(max_digits=10, decimal_places=2)
    ipvaPago = models.BooleanField(default=False)
    disponivel = models.BooleanField(default=True)
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT, related_name='veiculos')
    categoria = models.ForeignKey(CategoriaVeiculo, on_delete=models.PROTECT, related_name='veiculos')

    def atualizarDisponibilidade(self, disponivel):
        self.disponivel = disponivel
        self.save(update_fields=['disponivel'])

    def __str__(self):
        return f"{self.modelo} ({self.placa})"
