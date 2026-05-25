from rest_framework import serializers

from .models import ItemAdicional


class ItemAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAdicional
        fields = ['id', 'reserva', 'adicional', 'quantidade']
