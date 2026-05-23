from django.db import models

from apps.pessoa.models import Pessoa


class Funcionario(Pessoa):
    matricula = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=60)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dataContratacao = models.DateField()

    def __str__(self):
        return f"{self.matricula} - {self.nome}"
