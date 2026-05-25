from django.db import models


class Agencia(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
