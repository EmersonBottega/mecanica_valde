from django.urls import path
from .views import ClienteListCreateView, ClienteDetailView, AutomovelListCreateView, AutomovelDetailView, ServicoListCreateView, ServicoDetailView, index, ClienteCreateView, AutomovelCreateView, ServicoCreateView

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list'),  # Suporte a busca por nome com '?search='
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    
    path('automoveis/', AutomovelListCreateView.as_view(), name='automovel-list'),
    path('automoveis/<int:pk>/', AutomovelDetailView.as_view(), name='automovel-detail'),
    
    path('servicos/', ServicoListCreateView.as_view(), name='servico-list'),
    path('servicos/<int:pk>/', ServicoDetailView.as_view(), name='servico-detail'),
    
    # Caminhos para o Front-end personalizado
    path('', index, name='index'),
    path('clientes/cadastrar/', ClienteCreateView.as_view(), name='cliente-create'),
    path('automoveis/cadastrar/', AutomovelCreateView.as_view(), name='automovel-create'),
    path('servicos/cadastrar/', ServicoCreateView.as_view(), name='servico-create'),
]
