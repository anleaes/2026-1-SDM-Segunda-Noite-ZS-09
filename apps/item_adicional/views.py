from rest_framework import viewsets

from .models import ItemAdicional
from .serializer import ItemAdicionalSerializer


class ItemAdicionalViewSet(viewsets.ModelViewSet):
    queryset = ItemAdicional.objects.all().order_by('id')

    serializer_class = ItemAdicionalSerializer
