from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.reserva.models import Reserva
from apps.adicional.models import Adicional
from .models import ItemAdicional
from .serializer import ItemAdicionalSerializer


class ItemAdicionalViewSet(viewsets.ModelViewSet):
    queryset = ItemAdicional.objects.all().order_by('id')
    serializer_class = ItemAdicionalSerializer


def item_list(request):
    pagina = 'item_adicional/list_item.html'
    todos_itens = ItemAdicional.objects.all().order_by('id')
    todas_reservas = Reserva.objects.all().order_by('id')
    todos_adicionais = Adicional.objects.all().order_by('id')
    dados_para_tela = {
        'itens': todos_itens,
        'reservas': todas_reservas,
        'adicionais': todos_adicionais
    }
    return render(request, pagina, dados_para_tela)


def item_create(request):
    if request.method == 'POST':
        id_da_reserva = request.POST['reserva_id']
        id_do_adicional = request.POST['adicional_id']
        quantidade_digitada = request.POST['quantidade']

        if id_da_reserva and id_do_adicional and quantidade_digitada:
            reserva_encontrada = get_object_or_404(Reserva, id=id_da_reserva)
            adicional_encontrado = get_object_or_404(Adicional, id=id_do_adicional)
            
            item_adicional, criado_agora = ItemAdicional.objects.get_or_create(
                reserva=reserva_encontrada,
                adicional=adicional_encontrado,
                defaults={'quantidade': quantidade_digitada}
            )
            if not criado_agora:
                item_adicional.quantidade = int(quantidade_digitada)
                item_adicional.save()
                
    return redirect('item_list')


def item_delete(request, id):
    item_para_deletar = get_object_or_404(ItemAdicional, id=id)
    item_para_deletar.delete()
    return redirect('item_list')
