from rest_framework import viewsets

from .models import Funcionario
from .serializer import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by('matricula')
    serializer_class = FuncionarioSerializer
