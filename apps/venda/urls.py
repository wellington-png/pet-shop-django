from django.urls import path
from apps.venda.views import (
    CompraCreateView,
    CompraListView,
    ProdutoCreateView,
    ProdutoListView,
    ProdutoDeleteView,
    ProdutoUpdateView,
    CompraUpdateView,
    CompraDeleteView,
    get_produto_value,
)

app_name = "venda"

urlpatterns = [
    path("compra/list/", CompraListView.as_view(), name="compra_list"),
    path("compra/create/", CompraCreateView.as_view(), name="compra_create"),
    path("compra/update/<int:pk>/", CompraUpdateView.as_view(), name="compra_update"),
    path("compra/delete/<int:pk>/", CompraDeleteView.as_view(), name="compra_delete"),
    path("produto/list/", ProdutoListView.as_view(), name="produto_list"),
    path("produto/create/", ProdutoCreateView.as_view(), name="produto_create"),
    path(
        "produto/update/<int:pk>/", ProdutoUpdateView.as_view(), name="produto_update"
    ),
    path("produto/get_value/<int:pk>/", get_produto_value, name="get_produto_value"),
    path(
        "produto/delete/<int:pk>/", ProdutoDeleteView.as_view(), name="produto_delete"
    ),
]
