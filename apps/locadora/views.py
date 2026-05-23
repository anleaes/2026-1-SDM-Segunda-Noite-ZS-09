from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView


class PessoaViewSet(APIView):
    def get(self, request):
        return Response(
            {'detail': 'Pessoa é uma classe abstrata. Use /api/clientes/ ou /api/funcionarios/.'},
            status=status.HTTP_200_OK,
        )
