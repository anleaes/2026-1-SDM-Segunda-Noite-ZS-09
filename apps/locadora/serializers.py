from rest_framework import serializers


class PessoaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    cpf = serializers.CharField(max_length=14)
    data_nascimento = serializers.DateField()
    email = serializers.EmailField(required=False, default='')
