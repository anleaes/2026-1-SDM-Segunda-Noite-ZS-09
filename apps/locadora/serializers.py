from rest_framework import serializers

from .models import CarteiraMotorista, Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'dataNascimento', 'ativo']


class CarteiraMotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarteiraMotorista
        fields = ['id', 'numeroRegistro', 'categoria', 'dataValidade', 'cliente']
