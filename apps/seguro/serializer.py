from rest_framework import serializers

from .models import Seguro


class SeguroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguro
        fields = ['id', 'franquia', 'valorDiaria', 'descricao']
        read_only_fields = ['id']


