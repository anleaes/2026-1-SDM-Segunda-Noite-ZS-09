from rest_framework import serializers


class PessoaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=120)
    cpf = serializers.CharField(max_length=14)
    dataNascimento = serializers.DateField()
