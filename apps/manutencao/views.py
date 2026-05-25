from rest_framework import viewsets

from .models import Manutencao
from .serializer import ManutencaoSerializer


class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all().order_by('dataManutencao')

    serializer_class = ManutencaoSerializer
