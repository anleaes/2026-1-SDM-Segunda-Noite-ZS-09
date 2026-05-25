from rest_framework import viewsets

from .models import CarteiraMotorista, Cliente, Funcionario
from .serializers import CarteiraMotoristaSerializer, ClienteSerializer, FuncionarioSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class CarteiraMotoristaViewSet(viewsets.ModelViewSet):
    queryset = CarteiraMotorista.objects.all()
    serializer_class = CarteiraMotoristaSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
