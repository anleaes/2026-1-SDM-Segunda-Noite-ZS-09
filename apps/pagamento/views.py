from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.reserva.models import Reserva
from .models import Pagamento
from .serializer import PagamentoSerializer


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all().order_by('id')

    serializer_class = PagamentoSerializer


def pagamento_list(request):
    pagina = 'pagamento/list_pagamento.html'
    todos_pagamentos = Pagamento.objects.all().order_by('id')
    reservas_sem_pagamento = Reserva.objects.filter(pagamento__isnull=True).order_by('id')
    dados_para_tela = {
        'pagamentos': todos_pagamentos,
        'reservas': reservas_sem_pagamento
    }
    return render(request, pagina, dados_para_tela)


def pagamento_create(request):
    if request.method == 'POST':
        data_digitada = request.POST.get('dataPagamento') or None
        valor_digitado = request.POST['valor']
        metodo_digitado = request.POST['metodoPagamento']
        status_digitado = request.POST.get('status') or 'PENDENTE'
        id_da_reserva = request.POST['reserva_id']

        if id_da_reserva and valor_digitado:
            reserva_encontrada = get_object_or_404(Reserva, id=id_da_reserva)
            Pagamento.objects.create(
                dataPagamento=data_digitada,
                valor=valor_digitado,
                metodoPagamento=metodo_digitado,
                status=status_digitado,
                reserva=reserva_encontrada
            )
    return redirect('pagamento_list')


def pagamento_delete(request, id):
    pagamento_para_deletar = get_object_or_404(Pagamento, id=id)
    pagamento_para_deletar.delete()
    return redirect('pagamento_list')
