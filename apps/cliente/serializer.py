from rest_framework import serializers

from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'dataNascimento', 'ativo']
        read_only_fields = ['id']
