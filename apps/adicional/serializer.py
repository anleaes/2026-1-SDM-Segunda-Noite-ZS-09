from rest_framework import serializers

from .models import Adicional


class AdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adicional
        fields = ['id', 'descricao', 'valorDiaria']
        read_only_fields = ['id']
