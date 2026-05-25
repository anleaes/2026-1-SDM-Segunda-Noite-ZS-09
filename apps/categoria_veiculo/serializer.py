from rest_framework import serializers

from .models import CategoriaVeiculo


class CategoriaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVeiculo
        fields = ['id', 'nome', 'descricao', 'capacidadePassageiros', 'valorAdicional']
        read_only_fields = ['id']
