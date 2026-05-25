from rest_framework import viewsets

from .models import Adicional
from .serializer import AdicionalSerializer


class AdicionalViewSet(viewsets.ModelViewSet):
    queryset = Adicional.objects.all().order_by('id')
    serializer_class = AdicionalSerializer
