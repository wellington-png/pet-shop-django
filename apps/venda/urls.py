from django.urls import path
from apps.venda.views import CompraCreateView, CompraListView

app_name = 'venda'

urlpatterns = [
    path('compra/list/', CompraListView.as_view(), name='compra_list'),
    path('compra/create/', CompraCreateView.as_view(), name='compra_create'),
]