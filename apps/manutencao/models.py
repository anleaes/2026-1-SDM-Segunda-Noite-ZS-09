from django.db import models

from apps.veiculo.models import Veiculo


class Manutencao(models.Model):
    dataManutencao = models.DateField()
    descricao = models.CharField(max_length=200)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='EM_ANDAMENTO')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, related_name='manutencoes')

    def finalizarManutencao(self):
        self.status = 'CONCLUIDA'
        self.save(update_fields=['status'])
        return True

    def __str__(self):
        return f"Manutencao {self.id} - Veiculo {self.veiculo.placa}"
