from django.db import models

from apps.reserva.models import Reserva


class Multa(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    dataInfracao = models.DateField()
    pago = models.BooleanField(default=False)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='multas')

    def registrarPagamento(self):
        self.pago = True
        self.save(update_fields=['pago'])
        return True

    def __str__(self):
        return f"Multa {self.id} - Valor: {self.valor} - Reserva {self.reserva.id}"
