from rest_framework import viewsets

from .models import CategoriaVeiculo
from .serializer import CategoriaVeiculoSerializer


class CategoriaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVeiculo.objects.all().order_by('nome')
    serializer_class = CategoriaVeiculoSerializer
