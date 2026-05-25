from django.db import models

class Adicional(models.Model):
    descricao = models.CharField(max_length=200)
    valorDiaria = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao
