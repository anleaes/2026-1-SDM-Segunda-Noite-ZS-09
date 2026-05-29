from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from apps.usuarios.decorators import login_obrigatorio

from apps.agencia.models import Agencia
from .models import Funcionario
from .serializer import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by('matricula')
    serializer_class = FuncionarioSerializer


@login_obrigatorio
def funcionario_list(request):
    pagina = 'funcionario/list_funcionario.html'
    todos_funcionarios = Funcionario.objects.all().order_by('id')
    todas_agencias = Agencia.objects.all().order_by('id')
    dados_para_tela = {
        'funcionarios': todos_funcionarios,
        'agencias': todas_agencias
    }
    return render(request, pagina, dados_para_tela)


@login_obrigatorio
def funcionario_create(request):
    if request.method == 'POST':
        nome_digitado = request.POST['nome']
        cpf_digitado = request.POST['cpf']
        data_nascimento_digitada = request.POST['dataNascimento']
        matricula_digitada = request.POST['matricula']
        cargo_digitado = request.POST['cargo']
        salario_digitado = request.POST['salario']
        data_contratacao_digitada = request.POST['dataContratacao']
        id_da_agencia = request.POST.get('agencia_id')

        agencia_escolhida = None
        if id_da_agencia:
            agencia_escolhida = get_object_or_404(Agencia, id=id_da_agencia)

        Funcionario.objects.create(
            nome=nome_digitado,
            cpf=cpf_digitado,
            dataNascimento=data_nascimento_digitada,
            matricula=matricula_digitada,
            cargo=cargo_digitado,
            salario=salario_digitado,
            dataContratacao=data_contratacao_digitada,
            agencia=agencia_escolhida
        )
    return redirect('funcionario_list')


@login_obrigatorio
def funcionario_delete(request, id):
    funcionario_para_deletar = get_object_or_404(Funcionario, id=id)
    funcionario_para_deletar.delete()
    return redirect('funcionario_list')
