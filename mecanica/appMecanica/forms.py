from django import forms
from .models import Cliente, Automovel, Servico

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email']

class AutomovelForm(forms.ModelForm):
    class Meta:
        model = Automovel
        fields = ['cliente', 'carro', 'placa', 'cor']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['automovel', 'descricao', 'valor']
