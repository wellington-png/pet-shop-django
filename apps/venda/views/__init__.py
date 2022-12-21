from apps.venda.views.venda_views import (
    CompraCreateView,
    CompraListView,
    CompraUpdateView,
    CompraDeleteView,
)
from apps.venda.views.produto_views import (
    ProdutoCreateView,
    ProdutoListView,
    ProdutoUpdateView,
)

__all__ = [
    "CompraCreateView",
    "CompraListView",
    "ProdutoCreateView",
    "ProdutoListView",
    "ProdutoUpdateView",
    "CompraUpdateView",
    "CompraDeleteView",
]
