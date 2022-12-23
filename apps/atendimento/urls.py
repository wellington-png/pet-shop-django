from django.urls import path
from apps.atendimento.views import (
    ConsultaCreateView,
    ConsultaListView,
    ConsultaDeleteView,
    ConsultaUpdateView,
    
    ServicoCreateView,
    ServicoListView,
    ServicoDeleteView,
    ServicoUpdateView,

    TipoServicoCreateView,
    TipoServicoListView,
    TipoServicoDeleteView,
    TipoServicoUpdateView,
)

app_name = "atendimento"

urlpatterns = [
    path("consulta/create/", ConsultaCreateView.as_view(), name="consulta_create"),
    path("consulta/list/", ConsultaListView.as_view(), name="consulta_list"),
    path("consulta/update/<int:pk>/", ConsultaUpdateView.as_view(), name="consulta_update"),
    path("servico/create/", ServicoCreateView.as_view(), name="servico_create"),
    path("servico/list/", ServicoListView.as_view(), name="servico_list"),
    path("servico/update/<int:pk>/", ServicoUpdateView.as_view(), name="servico_update"),
    path("tipo_servico/create/", TipoServicoCreateView.as_view(), name="tipo_servico_create"),
    path("tipo_servico/list/", TipoServicoListView.as_view(), name="tipo_servico_list"),
    path("tipo_servico/update/<int:pk>/", TipoServicoUpdateView.as_view(), name="tipo_servico_update"),
]