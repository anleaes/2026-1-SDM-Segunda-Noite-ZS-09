from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.cliente.models import Cliente
from .models import CarteiraMotorista
from .serializer import CarteiraMotoristaSerializer


class CarteiraMotoristaViewSet(viewsets.ModelViewSet):
    queryset = CarteiraMotorista.objects.all().order_by('id')
    serializer_class = CarteiraMotoristaSerializer


def carteira_list(request):
    pagina = 'carteira_motorista/list_carteira.html'
    todas_cnhs = CarteiraMotorista.objects.all().order_by('id')
    todos_clientes = Cliente.objects.all().order_by('id')
    dados_para_tela = {
        'carteiras': todas_cnhs,
        'clientes': todos_clientes
    }
    return render(request, pagina, dados_para_tela)


def carteira_create(request):
    if request.method == 'POST':
        numero_digitado = request.POST['numeroRegistro']
        categoria_escolhida = request.POST['categoria']
        data_digitada = request.POST['dataValidade']
        id_do_cliente = request.POST['cliente_id']

        if numero_digitado and categoria_escolhida and data_digitada and id_do_cliente:
            cliente_encontrado = get_object_or_404(Cliente, id=id_do_cliente)
            if not hasattr(cliente_encontrado, 'carteiraMotorista'):
                CarteiraMotorista.objects.create(
                    numeroRegistro=numero_digitado,
                    categoria=categoria_escolhida,
                    dataValidade=data_digitada,
                    cliente=cliente_encontrado
                )
    return redirect('carteira_list')


def carteira_delete(request, id):
    cnh_para_deletar = get_object_or_404(CarteiraMotorista, id=id)
    cnh_para_deletar.delete()
    return redirect('carteira_list')
