from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.usuarios.decorators import login_obrigatorio

from .models import Agencia
from .serializer import AgenciaSerializer


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all().order_by('nome')
    serializer_class = AgenciaSerializer


@login_obrigatorio
def agencia_list(request):
    pagina = 'agencia/list_agencia.html'
    todas_agencias = Agencia.objects.all().order_by('id')
    dados_para_tela = {
        'agencias': todas_agencias
    }
    return render(request, pagina, dados_para_tela)


@login_obrigatorio
def agencia_create(request):
    if request.method == 'POST':
        nome_digitado = request.POST['nome']
        endereco_digitado = request.POST['endereco']
        telefone_digitado = request.POST['telefone']
        esta_ativa = 'ativa' in request.POST

        Agencia.objects.create(
            nome=nome_digitado,
            endereco=endereco_digitado,
            telefone=telefone_digitado,
            ativa=esta_ativa
        )
    return redirect('agencia_list')


@login_obrigatorio
def agencia_delete(request, id):
    agencia_para_deletar = get_object_or_404(Agencia, id=id)
    agencia_para_deletar.delete()
    return redirect('agencia_list')
