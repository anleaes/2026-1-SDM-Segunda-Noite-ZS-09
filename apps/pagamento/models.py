from django.db import models
from django.utils import timezone

from apps.reserva.models import Reserva


class Pagamento(models.Model):
    dataPagamento = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodoPagamento = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='PENDENTE')
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='pagamento')

    def processarPagamento(self):
        self.status = 'PAGO'
        self.dataPagamento = timezone.now().date()
        self.save(update_fields=['status', 'dataPagamento'])
        return True

    def estornarPagamento(self):
        self.status = 'ESTORNADO'
        self.save(update_fields=['status'])
        return True

    def __str__(self):
        return f"Pagamento {self.id} - Reserva {self.reserva.id}"
