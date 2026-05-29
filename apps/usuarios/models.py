from django.db import models


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=120)
    email = models.EmailField('Email', unique=True)
    senha = models.CharField('Senha', max_length=50)

    def login(self, senha):
        return self.senha == senha

    def __str__(self):
        return self.nome
