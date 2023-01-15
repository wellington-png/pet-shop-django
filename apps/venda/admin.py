from django.contrib.admin import ModelAdmin, register, TabularInline

from apps.venda.models import Compra, ItemCompra, Produto, Estoque


class ItemCompraInline(TabularInline):
    model = ItemCompra
    extra = 1


@register(Produto)
class ProdutoAdmin(ModelAdmin):
    pass


@register(Compra)
class CompraAdmin(ModelAdmin):
    inlines = [ItemCompraInline]
    list_display = ["cliente", "atendente", "data_compra", "valor_total"]


@register(Estoque)
class EstoqueAdmin(ModelAdmin):
    pass


@register(ItemCompra)
class ItemCompraAdmin(ModelAdmin):
    list_display = ["produto", "quantidade"]
