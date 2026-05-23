from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField('E-mail', blank=True, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.nome} ({self.cpf})'


class Cliente(Pessoa):
    ativo = models.BooleanField('Ativo', default=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, default='')
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    observacoes = models.TextField('Observações', blank=True, default='')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def verificar_elegibilidade_locacao(self):
        if not self.ativo:
            return False
        try:
            return self.carteira_motorista.is_valida()
        except CarteiraMotorista.DoesNotExist:
            return False

    def __str__(self):
        return self.nome
