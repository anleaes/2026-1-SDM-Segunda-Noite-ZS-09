from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from apps.usuarios.decorators import login_obrigatorio


class PessoaInfoView(APIView):
    def get(self, request):
        data = {
            'classe': 'Pessoa',
            'tipo': 'abstract',
            'atributos': ['nome', 'cpf', 'dataNascimento'],
        }
        return Response(data, status=status.HTTP_200_OK)


@login_obrigatorio
def pessoa_info(request):
    template_name = 'pessoa/info_pessoa.html'
    context = {
        'classe': 'Pessoa',
        'tipo': 'Abstrata',
        'atributos': ['nome', 'cpf', 'dataNascimento'],
        'descendentes': ['Cliente', 'Funcionario']
    }
    return render(request, template_name, context)
