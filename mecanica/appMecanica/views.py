from rest_framework import generics
from .models import Cliente, Automovel, Servico
from .serializers import ClienteSerializer, AutomovelSerializer, ServicoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from .forms import ClienteForm, AutomovelForm, ServicoForm

# Listar e criar clientes
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']  # Permite buscar clientes pelo campo nome

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


# Página principal (index)
def index(request):
    return render(request, 'appMecanica/index.html')

# View para criar Cliente
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'appMecanica/cliente_form.html'

    def get_success_url(self):
        return reverse('automovel-create')

# View para criar Automóvel
class AutomovelCreateView(CreateView):
    model = Automovel
    form_class = AutomovelForm
    template_name = 'appMecanica/automovel_form.html'

    def get_success_url(self):
        return reverse('servico-create')

# View para criar Serviço
class ServicoCreateView(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'appMecanica/servico_form.html'

    def get_success_url(self):
        return reverse('index')
