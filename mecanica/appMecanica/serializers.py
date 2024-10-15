from rest_framework import serializers
from .models import Cliente, Automovel, Servico

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class AutomovelSerializer(serializers.ModelSerializer):
    servicos = ServicoSerializer(many=True, read_only=True)

    class Meta:
        model = Automovel
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    automoveis = AutomovelSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'
