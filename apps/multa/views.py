from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.reserva.models import Reserva
from .models import Multa
from .serializer import MultaSerializer


class MultaViewSet(viewsets.ModelViewSet):
    queryset = Multa.objects.all().order_by('dataInfracao')
    serializer_class = MultaSerializer


def multa_list(request):
    pagina = 'multa/list_multa.html'
    todas_multas = Multa.objects.all().order_by('id')
    todas_reservas = Reserva.objects.all().order_by('id')
    dados_para_tela = {
        'multas': todas_multas,
        'reservas': todas_reservas
    }
    return render(request, pagina, dados_para_tela)


def multa_create(request):
    if request.method == 'POST':
        valor_digitado = request.POST['valor']
        descricao_digitada = request.POST['descricao']
        data_digitada = request.POST['dataInfracao']
        esta_pago = 'pago' in request.POST
        id_da_reserva = request.POST['reserva_id']

        if valor_digitado and descricao_digitada and data_digitada and id_da_reserva:
            reserva_encontrada = get_object_or_404(Reserva, id=id_da_reserva)
            Multa.objects.create(
                valor=valor_digitado,
                descricao=descricao_digitada,
                dataInfracao=data_digitada,
                pago=esta_pago,
                reserva=reserva_encontrada
            )
    return redirect('multa_list')


def multa_delete(request, id):
    multa_para_deletar = get_object_or_404(Multa, id=id)
    multa_para_deletar.delete()
    return redirect('multa_list')
