from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from .models import Adicional
from .serializer import AdicionalSerializer


class AdicionalViewSet(viewsets.ModelViewSet):
    queryset = Adicional.objects.all().order_by('id')
    serializer_class = AdicionalSerializer


def adicional_list(request):
    pagina = 'adicional/list_adicional.html'
    todos_adicionais = Adicional.objects.all().order_by('id')
    dados_para_tela = {
        'adicionais': todos_adicionais
    }
    return render(request, pagina, dados_para_tela)


def adicional_create(request):
    if request.method == 'POST':
        descricao_digitada = request.POST['descricao']
        valor_digitado = request.POST['valorDiaria']
        
        Adicional.objects.create(
            descricao=descricao_digitada,
            valorDiaria=valor_digitado
        )
    return redirect('adicional_list')


def adicional_delete(request, id):
    adicional_para_deletar = get_object_or_404(Adicional, id=id)
    adicional_para_deletar.delete()
    return redirect('adicional_list')
