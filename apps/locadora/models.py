from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField('E-mail', blank=True, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome
