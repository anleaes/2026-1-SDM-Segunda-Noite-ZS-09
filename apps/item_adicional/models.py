from django.db import models

from apps.reserva.models import Reserva
from apps.adicional.models import Adicional


class ItemAdicional(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='itens_adicionais')
    adicional = models.ForeignKey(Adicional, on_delete=models.PROTECT, related_name='itens_adicionais')
    quantidade = models.PositiveIntegerField()

    class Meta:
        unique_together = ('reserva', 'adicional')

    def __str__(self):
        return f"{self.quantidade}x {self.adicional.descricao} na Reserva {self.reserva.id}"
