from rest_framework import serializers

from .models import Manutencao


class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = ['id', 'dataManutencao', 'descricao', 'custo', 'status', 'veiculo']
        read_only_fields = ['id']

