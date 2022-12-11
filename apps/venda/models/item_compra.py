from django.db.models import ForeignKey, CASCADE, PositiveIntegerField

from apps.core.models import BaseModel


class ItemCompra(BaseModel):
    compra = ForeignKey('venda.Compra', verbose_name='Compra', on_delete=CASCADE)
    produto = ForeignKey('venda.Produto', verbose_name='Produto', on_delete=CASCADE)
    quantidade = PositiveIntegerField(verbose_name='Quantidade')

    class Meta:
        verbose_name = 'Item Compra'
        verbose_name_plural = 'Itens Compra'

    def __str__(self):
        return self.produto.nome