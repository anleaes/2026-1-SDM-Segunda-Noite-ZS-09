from rest_framework import viewsets

from .models import Agencia
from .serializer import AgenciaSerializer


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all().order_by('nome')
    serializer_class = AgenciaSerializer
