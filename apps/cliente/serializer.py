from rest_framework import serializers

from apps.carteira_motorista.models import CarteiraMotorista
from .models import Cliente


class CarteiraMotoristaResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarteiraMotorista
        fields = ['id', 'numeroRegistro', 'categoria', 'dataValidade']


class ReservaResumoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    dataReserva = serializers.DateField()
    dataInicio = serializers.DateField()
    dataFim = serializers.DateField()
    valorTotal = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField()


class MultaResumoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    valor = serializers.DecimalField(max_digits=10, decimal_places=2)
    descricao = serializers.CharField()
    dataInfracao = serializers.DateField()
    pago = serializers.BooleanField()


class ClienteSerializer(serializers.ModelSerializer):
    carteiraMotorista = CarteiraMotoristaResumoSerializer(read_only=True)
    reservas = ReservaResumoSerializer(many=True, read_only=True)
    multas = serializers.SerializerMethodField()

    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'dataNascimento', 'ativo',
                  'carteiraMotorista', 'reservas', 'multas']
        read_only_fields = ['id']

    def get_multas(self, obj):
        # Multa do colega aponta para Reserva, então pegamos as multas via reservas do cliente
        from apps.multa.models import Multa
        multas = Multa.objects.filter(reserva__cliente=obj)
        return MultaResumoSerializer(multas, many=True).data
