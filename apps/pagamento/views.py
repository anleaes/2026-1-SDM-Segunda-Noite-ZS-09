from rest_framework import viewsets

from .models import Pagamento
from .serializer import PagamentoSerializer


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all().order_by('id')

    serializer_class = PagamentoSerializer
