from django.db import models

from apps.agencia.models import Agencia
from apps.pessoa.models import Pessoa


class Funcionario(Pessoa):
    matricula = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=60)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dataContratacao = models.DateField()
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT, related_name='funcionarios', null=True, blank=True)

    def __str__(self):
        return f"{self.matricula} - {self.nome}"
