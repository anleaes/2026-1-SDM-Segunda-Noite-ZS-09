from rest_framework import serializers

from apps.manutencao.models import Manutencao
from .models import Veiculo


class ManutencaoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = ['id', 'dataManutencao', 'descricao', 'custo', 'status']


class ReservaResumoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    dataReserva = serializers.DateField()
    dataInicio = serializers.DateField()
    dataFim = serializers.DateField()
    status = serializers.CharField()


class VeiculoSerializer(serializers.ModelSerializer):
    manutencoes = ManutencaoResumoSerializer(many=True, read_only=True)
    reservas = ReservaResumoSerializer(many=True, read_only=True)

    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'modelo', 'ano', 'valorDiaria', 'ipvaPago', 'disponivel',
                  'agencia', 'categoria', 'manutencoes', 'reservas']
        read_only_fields = ['id']
