from apps.atendimento.views.consulta_views import (
    ConsultaCreateView,
    ConsultaListView,
    ConsultaUpdateView,
    ConsultaDeleteView,
)
from apps.atendimento.views.servico_views import (
    ServicoCreateView,
    ServicoListView,
    ServicoUpdateView,
    ServicoDeleteView,
)
from apps.atendimento.views.tipo_servico_views import (
    TipoServicoCreateView,
    TipoServicoListView,
    TipoServicoUpdateView,
    TipoServicoDeleteView,
    get_servico_value
)

__all__ = [
    "ConsultaCreateView",
    "ConsultaListView",
    "ConsultaUpdateView",
    "ConsultaDeleteView",
    "ServicoCreateView",
    "ServicoListView",
    "ServicoUpdateView",
    "ServicoDeleteView",
    "TipoServicoCreateView",
    "TipoServicoListView",
    "TipoServicoUpdateView",
    "TipoServicoDeleteView",
    "get_servico_value"
]
