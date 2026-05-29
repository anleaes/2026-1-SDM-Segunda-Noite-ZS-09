from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.agencia.models import Agencia
from apps.cliente.models import Cliente
from apps.veiculo.models import Veiculo
from .models import Reserva
from .serializer import ReservaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all().order_by('dataReserva')

    serializer_class = ReservaSerializer


def reserva_list(request):
    pagina = 'reserva/list_reserva.html'
    todas_reservas = Reserva.objects.all().order_by('id')
    todos_clientes = Cliente.objects.all().order_by('id')
    todos_veiculos = Veiculo.objects.all().order_by('id')
    todas_agencias = Agencia.objects.all().order_by('id')
    dados_para_tela = {
        'reservas': todas_reservas,
        'clientes': todos_clientes,
        'veiculos': todos_veiculos,
        'agencias': todas_agencias
    }
    return render(request, pagina, dados_para_tela)


def reserva_create(request):
    if request.method == 'POST':
        data_reserva_digitada = request.POST['dataReserva']
        data_inicio_digitada = request.POST['dataInicio']
        data_fim_digitada = request.POST['dataFim']
        valor_digitado = request.POST.get('valorTotal') or 0
        status_digitado = request.POST.get('status') or 'ATIVA'
        id_do_cliente = request.POST['cliente_id']
        id_do_veiculo = request.POST['veiculo_id']
        id_da_agencia = request.POST['agencia_id']

        if id_do_cliente and id_do_veiculo and id_da_agencia:
            cliente_encontrado = get_object_or_404(Cliente, id=id_do_cliente)
            veiculo_encontrado = get_object_or_404(Veiculo, id=id_do_veiculo)
            agencia_encontrada = get_object_or_404(Agencia, id=id_da_agencia)
            Reserva.objects.create(
                dataReserva=data_reserva_digitada,
                dataInicio=data_inicio_digitada,
                dataFim=data_fim_digitada,
                valorTotal=valor_digitado,
                status=status_digitado,
                cliente=cliente_encontrado,
                veiculo=veiculo_encontrado,
                agencia=agencia_encontrada
            )
    return redirect('reserva_list')


def reserva_delete(request, id):
    reserva_para_deletar = get_object_or_404(Reserva, id=id)
    reserva_para_deletar.delete()
    return redirect('reserva_list')
