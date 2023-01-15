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
    get_servico_value
)

app_name = "atendimento"

urlpatterns = [
    path("consulta/create/", ConsultaCreateView.as_view(), name="consulta_create"),
    path("consulta/list/", ConsultaListView.as_view(), name="consulta_list"),
    path("consulta/update/<int:pk>/", ConsultaUpdateView.as_view(), name="consulta_update"),
    path("consulta/delete/<int:pk>/", ConsultaDeleteView.as_view(), name="consulta_delete"),
    
    path("servico/create/", ServicoCreateView.as_view(), name="servico_create"),
    path("servico/list/", ServicoListView.as_view(), name="servico_list"),
    path("servico/update/<int:pk>/", ServicoUpdateView.as_view(), name="servico_update"),
    path("servico/delete/<int:pk>/", ServicoDeleteView.as_view(), name="servico_delete"),
    
    path("tipo_servico/create/", TipoServicoCreateView.as_view(), name="tipo_servico_create"),
    path("tipo_servico/list/", TipoServicoListView.as_view(), name="tipo_servico_list"),
    path("tipo_servico/update/<int:pk>/", TipoServicoUpdateView.as_view(), name="tipo_servico_update"),
    path("tipo_servico/delete/<int:pk>/", TipoServicoDeleteView.as_view(), name="tipo_servico_delete"),
    path("servico/get_value/<int:pk>/", get_servico_value, name="get_servico_value"),
    
]
