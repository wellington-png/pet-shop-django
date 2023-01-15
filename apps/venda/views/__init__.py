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
    ProdutoDeleteView,
    get_produto_value
)

__all__ = [
    "CompraCreateView",
    "CompraListView",
    "ProdutoCreateView",
    "ProdutoListView",
    "ProdutoUpdateView",
    "CompraUpdateView",
    "CompraDeleteView",
    "get_produto_value",
    "ProdutoDeleteView",
]
