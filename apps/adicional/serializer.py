from rest_framework import serializers

from apps.item_adicional.models import ItemAdicional
from .models import Adicional


class ItemAdicionalResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAdicional
        fields = ['id', 'reserva', 'quantidade']


class AdicionalSerializer(serializers.ModelSerializer):
    itens_adicionais = ItemAdicionalResumoSerializer(many=True, read_only=True)

    class Meta:
        model = Adicional
        fields = ['id', 'descricao', 'valorDiaria', 'itens_adicionais']
        read_only_fields = ['id']
