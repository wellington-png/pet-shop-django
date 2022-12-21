from django.urls import path
from apps.venda.views import CompraCreateView, CompraListView, ProdutoCreateView, ProdutoListView, ProdutoUpdateView

app_name = 'venda'

urlpatterns = [
    path('compra/list/', CompraListView.as_view(), name='compra_list'),
    path('compra/create/', CompraCreateView.as_view(), name='compra_create'),
    path('produto/list/', ProdutoListView.as_view(), name='produto_list'),
    path('produto/create/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produto/update/<int:pk>/', ProdutoUpdateView.as_view(), name='produto_update'),
]