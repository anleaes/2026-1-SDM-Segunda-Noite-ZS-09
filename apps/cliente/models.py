from django.db import models

from apps.pessoa.models import Pessoa


class Cliente(Pessoa):
    ativo = models.BooleanField(default=True)

    def verificarElegibilidadeLocacao(self):
        return self.ativo

    def __str__(self):
        return self.nome
