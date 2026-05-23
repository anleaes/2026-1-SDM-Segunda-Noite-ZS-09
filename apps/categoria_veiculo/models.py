from django.db import models


class CategoriaVeiculo(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField(blank=True)
    capacidadePassageiros = models.PositiveIntegerField()
    valorAdicional = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.nome
