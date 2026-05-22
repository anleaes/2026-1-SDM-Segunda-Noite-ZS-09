from rest_framework import serializers

from .models import CarteiraMotorista


class CarteiraMotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarteiraMotorista
        fields = ['id', 'numeroRegistro', 'categoria', 'dataValidade', 'cliente']
