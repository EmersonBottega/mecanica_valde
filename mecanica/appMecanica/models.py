from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.nome

class Automovel(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='automoveis', on_delete=models.CASCADE)
    carro = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    cor = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.placa} {self.carro} ({self.cor}) - Cliente: {self.cliente.nome}'

class Servico(models.Model):
    automovel = models.ForeignKey(Automovel, related_name='servicos', on_delete=models.CASCADE)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_servico = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Serviço em {self.automovel.placa} {self.automovel.carro} - {self.data_servico}'

