from django.db import models

from apps.cliente.models import Cliente
from apps.veiculo.models import Veiculo
from apps.agencia.models import Agencia


class Reserva(models.Model):
    dataReserva = models.DateField()
    dataInicio = models.DateField()
    dataFim = models.DateField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, default='ATIVA')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='reservas')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, related_name='reservas')
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT, related_name='reservas')

    def calcularValorTotal(self):
        if self.dataInicio and self.dataFim and self.veiculo:
            dias = (self.dataFim - self.dataInicio).days
            if dias < 0:
                dias = 0
            self.valorTotal = dias * self.veiculo.valorDiaria
            self.save(update_fields=['valorTotal'])
        return self.valorTotal

    def confirmarReserva(self):
        self.status = 'CONFIRMADA'
        self.save(update_fields=['status'])

    def cancelarReserva(self):
        self.status = 'CANCELADA'
        self.save(update_fields=['status'])

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente.nome}"
