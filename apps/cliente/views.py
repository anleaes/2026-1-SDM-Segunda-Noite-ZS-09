from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.usuarios.decorators import login_obrigatorio

from .models import Cliente
from .serializer import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer


@login_obrigatorio
def cliente_list(request):
    pagina = 'cliente/list_cliente.html'
    todos_clientes = Cliente.objects.all().order_by('id')
    dados_para_tela = {
        'clientes': todos_clientes
    }
    return render(request, pagina, dados_para_tela)


@login_obrigatorio
def cliente_create(request):
    if request.method == 'POST':
        nome_digitado = request.POST['nome']
        cpf_digitado = request.POST['cpf']
        data_digitada = request.POST['dataNascimento']
        esta_ativo = 'ativo' in request.POST

        Cliente.objects.create(
            nome=nome_digitado,
            cpf=cpf_digitado,
            dataNascimento=data_digitada,
            ativo=esta_ativo
        )
    return redirect('cliente_list')


@login_obrigatorio
def cliente_delete(request, id):
    cliente_para_deletar = get_object_or_404(Cliente, id=id)
    cliente_para_deletar.delete()
    return redirect('cliente_list')
