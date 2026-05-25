from rest_framework import serializers

from apps.funcionario.models import Funcionario
from apps.veiculo.models import Veiculo
from .models import Agencia


class VeiculoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'modelo', 'ano', 'valorDiaria', 'disponivel']


class FuncionarioResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'matricula', 'cargo']


class AgenciaSerializer(serializers.ModelSerializer):
    veiculos = VeiculoResumoSerializer(many=True, read_only=True)
    funcionarios = FuncionarioResumoSerializer(many=True, read_only=True)

    class Meta:
        model = Agencia
        fields = ['id', 'nome', 'endereco', 'telefone', 'ativa',
                  'veiculos', 'funcionarios']
        read_only_fields = ['id']
