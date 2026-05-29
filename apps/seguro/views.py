from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from .models import Seguro
from .serializer import SeguroSerializer


class SeguroViewSet(viewsets.ModelViewSet):
    queryset = Seguro.objects.all().order_by('id')
    serializer_class = SeguroSerializer


def seguro_list(request):
    pagina = 'seguro/list_seguro.html'
    todos_seguros = Seguro.objects.all().order_by('id')
    dados_para_tela = {
        'seguros': todos_seguros
    }
    return render(request, pagina, dados_para_tela)


def seguro_create(request):
    if request.method == 'POST':
        franquia_digitada = request.POST['franquia']
        valor_digitado = request.POST['valorDiaria']
        descricao_digitada = request.POST['descricao']

        if franquia_digitada and valor_digitado and descricao_digitada:
            Seguro.objects.create(
                franquia=franquia_digitada,
                valorDiaria=valor_digitado,
                descricao=descricao_digitada
            )
    return redirect('seguro_list')


def seguro_delete(request, id):
    seguro_para_deletar = get_object_or_404(Seguro, id=id)
    seguro_para_deletar.delete()
    return redirect('seguro_list')
