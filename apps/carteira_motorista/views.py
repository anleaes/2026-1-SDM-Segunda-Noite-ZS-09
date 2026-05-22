from rest_framework import viewsets

from .models import CarteiraMotorista
from .serializer import CarteiraMotoristaSerializer


class CarteiraMotoristaViewSet(viewsets.ModelViewSet):
    queryset = CarteiraMotorista.objects.all().order_by('id')
    serializer_class = CarteiraMotoristaSerializer
