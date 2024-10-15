from django.urls import path
from .views import ClienteListCreateView, ClienteDetailView, AutomovelListCreateView, AutomovelDetailView, ServicoListCreateView, ServicoDetailView

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    
    path('automoveis/', AutomovelListCreateView.as_view(), name='automovel-list'),
    path('automoveis/<int:pk>/', AutomovelDetailView.as_view(), name='automovel-detail'),
    
    path('servicos/', ServicoListCreateView.as_view(), name='servico-list'),
    path('servicos/<int:pk>/', ServicoDetailView.as_view(), name='servico-detail'),
]
