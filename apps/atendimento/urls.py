from django.urls import path
from apps.atendimento.views import ConsultaCreateView, ConsultaListView, ServicoCreateView, ServicoListView

app_name = 'atendimento'

urlpatterns = [
    path('consulta/create/', ConsultaCreateView.as_view(), name='consulta_create'),
    path('consulta/list/', ConsultaListView.as_view(), name='consulta_list'),
    path('servico/create/', ServicoCreateView.as_view(), name='servico_create'),
    path('servico/list/', ServicoListView.as_view(), name='servico_list'),
]