from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)
    dataNascimento = models.DateField()

    class Meta:
        abstract = True
