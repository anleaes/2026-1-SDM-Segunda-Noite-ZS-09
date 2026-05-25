from rest_framework import serializers

from apps.veiculo.models import Veiculo
from .models import CategoriaVeiculo


class VeiculoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'modelo', 'ano', 'valorDiaria', 'disponivel']


class CategoriaVeiculoSerializer(serializers.ModelSerializer):
    veiculos = VeiculoResumoSerializer(many=True, read_only=True)

    class Meta:
        model = CategoriaVeiculo
        fields = ['id', 'nome', 'descricao', 'capacidadePassageiros', 'valorAdicional', 'veiculos']
        read_only_fields = ['id']
