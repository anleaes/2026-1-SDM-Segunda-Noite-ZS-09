from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.veiculo.models import Veiculo
from .models import Manutencao
from .serializer import ManutencaoSerializer


class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all().order_by('dataManutencao')

    serializer_class = ManutencaoSerializer


def manutencao_list(request):
    pagina = 'manutencao/list_manutencao.html'
    todas_manutencoes = Manutencao.objects.all().order_by('id')
    todos_veiculos = Veiculo.objects.all().order_by('id')
    dados_para_tela = {
        'manutencoes': todas_manutencoes,
        'veiculos': todos_veiculos
    }
    return render(request, pagina, dados_para_tela)


def manutencao_create(request):
    if request.method == 'POST':
        data_digitada = request.POST['dataManutencao']
        descricao_digitada = request.POST['descricao']
        custo_digitado = request.POST['custo']
        status_digitado = request.POST.get('status') or 'EM_ANDAMENTO'
        id_do_veiculo = request.POST['veiculo_id']

        if id_do_veiculo:
            veiculo_encontrado = get_object_or_404(Veiculo, id=id_do_veiculo)
            Manutencao.objects.create(
                dataManutencao=data_digitada,
                descricao=descricao_digitada,
                custo=custo_digitado,
                status=status_digitado,
                veiculo=veiculo_encontrado
            )
    return redirect('manutencao_list')


def manutencao_delete(request, id):
    manutencao_para_deletar = get_object_or_404(Manutencao, id=id)
    manutencao_para_deletar.delete()
    return redirect('manutencao_list')
