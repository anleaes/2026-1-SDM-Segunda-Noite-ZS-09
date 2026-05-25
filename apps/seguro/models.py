from django.db import models


class Seguro(models.Model):
    franquia = models.DecimalField(max_digits=10, decimal_places=2)
    valorDiaria = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao
