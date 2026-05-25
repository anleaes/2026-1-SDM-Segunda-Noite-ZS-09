from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PessoaInfoView(APIView):
    def get(self, request):
        data = {
            'classe': 'Pessoa',
            'tipo': 'abstract',
            'atributos': ['nome', 'cpf', 'dataNascimento'],
        }
        return Response(data, status=status.HTTP_200_OK)
