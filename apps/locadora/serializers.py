from rest_framework import serializers

from .models import Agencia, CarteiraMotorista, Cliente, Funcionario


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'dataNascimento', 'ativo']


class CarteiraMotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarteiraMotorista
        fields = ['id', 'numeroRegistro', 'categoria', 'dataValidade', 'cliente']


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'cpf', 'dataNascimento', 'matricula', 'cargo', 'salario', 'dataContratacao', 'agencia']


class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = ['id', 'nome', 'endereco', 'telefone', 'ativa']
