from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.usuarios.decorators import login_obrigatorio

from apps.agencia.models import Agencia
from apps.categoria_veiculo.models import CategoriaVeiculo
from .models import Veiculo
from .serializer import VeiculoSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all().order_by('placa')
    serializer_class = VeiculoSerializer


@login_obrigatorio
def veiculo_list(request):
    pagina = 'veiculo/list_veiculo.html'
    todos_veiculos = Veiculo.objects.all().order_by('id')
    todas_agencias = Agencia.objects.all().order_by('id')
    todas_categorias = CategoriaVeiculo.objects.all().order_by('id')
    dados_para_tela = {
        'veiculos': todos_veiculos,
        'agencias': todas_agencias,
        'categorias': todas_categorias
    }
    return render(request, pagina, dados_para_tela)


@login_obrigatorio
def veiculo_create(request):
    if request.method == 'POST':
        placa_digitada = request.POST['placa']
        modelo_digitado = request.POST['modelo']
        ano_digitado = request.POST['ano']
        valor_digitado = request.POST['valorDiaria']
        ipva_pago = 'ipvaPago' in request.POST
        esta_disponivel = 'disponivel' in request.POST
        id_da_agencia = request.POST['agencia_id']
        id_da_categoria = request.POST['categoria_id']

        if placa_digitada and id_da_agencia and id_da_categoria:
            agencia_encontrada = get_object_or_404(Agencia, id=id_da_agencia)
            categoria_encontrada = get_object_or_404(CategoriaVeiculo, id=id_da_categoria)
            Veiculo.objects.create(
                placa=placa_digitada,
                modelo=modelo_digitado,
                ano=ano_digitado,
                valorDiaria=valor_digitado,
                ipvaPago=ipva_pago,
                disponivel=esta_disponivel,
                agencia=agencia_encontrada,
                categoria=categoria_encontrada
            )
    return redirect('veiculo_list')


@login_obrigatorio
def veiculo_delete(request, id):
    veiculo_para_deletar = get_object_or_404(Veiculo, id=id)
    veiculo_para_deletar.delete()
    return redirect('veiculo_list')
