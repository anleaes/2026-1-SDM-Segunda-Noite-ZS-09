from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from .models import CategoriaVeiculo
from .serializer import CategoriaVeiculoSerializer


class CategoriaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVeiculo.objects.all().order_by('nome')
    serializer_class = CategoriaVeiculoSerializer


def categoria_list(request):
    pagina = 'categoria_veiculo/list_categoria.html'
    todas_categorias = CategoriaVeiculo.objects.all().order_by('id')
    dados_para_tela = {
        'categorias': todas_categorias
    }
    return render(request, pagina, dados_para_tela)


def categoria_create(request):
    if request.method == 'POST':
        nome_digitado = request.POST['nome']
        descricao_digitada = request.POST['descricao']
        capacidade_digitada = request.POST['capacidadePassageiros']
        valor_digitado = request.POST['valorAdicional']

        CategoriaVeiculo.objects.create(
            nome=nome_digitado,
            descricao=descricao_digitada,
            capacidadePassageiros=capacidade_digitada,
            valorAdicional=valor_digitado
        )
    return redirect('categoria_list')


def categoria_delete(request, id):
    categoria_para_deletar = get_object_or_404(CategoriaVeiculo, id=id)
    categoria_para_deletar.delete()
    return redirect('categoria_list')
