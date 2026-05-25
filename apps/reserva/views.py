from rest_framework import viewsets

from .models import Reserva
from .serializer import ReservaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all().order_by('dataReserva')

    serializer_class = ReservaSerializer
