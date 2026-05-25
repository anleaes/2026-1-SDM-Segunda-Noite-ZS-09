from rest_framework import serializers

from .models import Pagamento


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['id', 'dataPagamento', 'valor', 'metodoPagamento', 'status', 'reserva']
        read_only_fields = ['id']

