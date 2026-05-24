from rest_framework import serializers

from .models import Veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'modelo', 'ano', 'valorDiaria', 'ipvaPago', 'disponivel', 'agencia', 'categoria']
        read_only_fields = ['id']
