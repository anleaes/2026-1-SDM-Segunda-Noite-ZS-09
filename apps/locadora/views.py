from rest_framework import viewsets

from .models import CarteiraMotorista, Cliente
from .serializers import CarteiraMotoristaSerializer, ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class CarteiraMotoristaViewSet(viewsets.ModelViewSet):
    queryset = CarteiraMotorista.objects.all()
    serializer_class = CarteiraMotoristaSerializer
