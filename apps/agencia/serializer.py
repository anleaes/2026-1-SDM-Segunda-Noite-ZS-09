from rest_framework import serializers

from .models import Agencia


class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = ['id', 'nome', 'endereco', 'telefone', 'ativa']
        read_only_fields = ['id']
