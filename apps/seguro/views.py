from rest_framework import viewsets

from .models import Seguro
from .serializer import SeguroSerializer


class SeguroViewSet(viewsets.ModelViewSet):
    queryset = Seguro.objects.all()
    serializer_class = SeguroSerializer
