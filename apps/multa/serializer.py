from rest_framework import serializers

from .models import Multa


class MultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multa
        fields = ['id', 'valor', 'descricao', 'dataInfracao', 'pago', 'reserva']
        read_only_fields = ['id']

