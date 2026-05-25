from django.db import models
from django.utils import timezone


class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)
    dataNascimento = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nome} ({self.cpf})"


class Cliente(Pessoa):
    ativo = models.BooleanField(default=True)

    def verificarElegibilidadeLocacao(self):
        return self.ativo


class CarteiraMotorista(models.Model):
    numeroRegistro = models.CharField(max_length=20, unique=True)
    categoria = models.CharField(max_length=5)
    dataValidade = models.DateField()
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='carteiraMotorista')

    def isValida(self):
        return self.dataValidade >= timezone.now().date()

    def __str__(self):
        return f"CNH {self.numeroRegistro} ({self.categoria})"


class Agencia(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Funcionario(Pessoa):
    matricula = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=60)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dataContratacao = models.DateField()
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT, related_name='funcionarios', null=True, blank=True)


class CategoriaVeiculo(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField(blank=True)
    capacidadePassageiros = models.PositiveIntegerField()
    valorAdicional = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.nome
