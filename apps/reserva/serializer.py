from rest_framework import serializers

from apps.item_adicional.models import ItemAdicional
from apps.multa.models import Multa
from apps.pagamento.models import Pagamento
from .models import Reserva


class PagamentoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['id', 'dataPagamento', 'valor', 'metodoPagamento', 'status']


class ItemAdicionalResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAdicional
        fields = ['id', 'adicional', 'quantidade']


class MultaResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multa
        fields = ['id', 'valor', 'descricao', 'dataInfracao', 'pago']


class ReservaSerializer(serializers.ModelSerializer):
    pagamento = PagamentoResumoSerializer(read_only=True)
    itens_adicionais = ItemAdicionalResumoSerializer(many=True, read_only=True)
    multas = MultaResumoSerializer(many=True, read_only=True)

    class Meta:
        model = Reserva
        fields = ['id', 'dataReserva', 'dataInicio', 'dataFim', 'valorTotal', 'status',
                  'cliente', 'veiculo', 'agencia',
                  'pagamento', 'itens_adicionais', 'multas']
        read_only_fields = ['id']
