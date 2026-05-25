from rest_framework import viewsets

from .models import Agencia, CarteiraMotorista, CategoriaVeiculo, Cliente, Funcionario
from .serializers import (
    AgenciaSerializer,
    CarteiraMotoristaSerializer,
    CategoriaVeiculoSerializer,
    ClienteSerializer,
    FuncionarioSerializer,
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class CarteiraMotoristaViewSet(viewsets.ModelViewSet):
    queryset = CarteiraMotorista.objects.all()
    serializer_class = CarteiraMotoristaSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer


class CategoriaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVeiculo.objects.all()
    serializer_class = CategoriaVeiculoSerializer
