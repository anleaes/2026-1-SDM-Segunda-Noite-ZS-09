from rest_framework import viewsets

from .models import Veiculo
from .serializer import VeiculoSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
