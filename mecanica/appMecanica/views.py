from rest_framework import generics
from .models import Cliente, Automovel, Servico
from .serializers import ClienteSerializer, AutomovelSerializer, ServicoSerializer

# Listar e criar clientes
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Detalhar, atualizar e deletar clientes
class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Listar e criar automóveis
class AutomovelListCreateView(generics.ListCreateAPIView):
    queryset = Automovel.objects.all()
    serializer_class = AutomovelSerializer

# Detalhar, atualizar e deletar automóveis
class AutomovelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Automovel.objects.all()
    serializer_class = AutomovelSerializer

# Listar e criar serviços
class ServicoListCreateView(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

# Detalhar, atualizar e deletar serviços
class ServicoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

