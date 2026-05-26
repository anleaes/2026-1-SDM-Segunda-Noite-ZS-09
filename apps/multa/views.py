from rest_framework import viewsets

from .models import Multa
from .serializer import MultaSerializer


class MultaViewSet(viewsets.ModelViewSet):
    queryset = Multa.objects.all().order_by('dataInfracao')

    serializer_class = MultaSerializer
