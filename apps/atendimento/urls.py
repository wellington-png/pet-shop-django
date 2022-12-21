from django.urls import path
from apps.atendimento.views import (
    ConsultaCreateView,
    ConsultaListView,
    ServicoCreateView,
    ServicoListView,
    TipoServicoCreateView,
    TipoServicoListView,
)

app_name = "atendimento"

urlpatterns = [
    path("consulta/create/", ConsultaCreateView.as_view(), name="consulta_create"),
    path("consulta/list/", ConsultaListView.as_view(), name="consulta_list"),
    path("servico/create/", ServicoCreateView.as_view(), name="servico_create"),
    path("servico/list/", ServicoListView.as_view(), name="servico_list"),
    path("tipo_servico/create/", TipoServicoCreateView.as_view(), name="tipo_servico_create"),
    path("tipo_servico/list/", TipoServicoListView.as_view(), name="tipo_servico_list"),
]
