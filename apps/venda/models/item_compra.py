from django.db.models import ForeignKey, CASCADE, PositiveIntegerField
from django.db.models.signals import pre_save
from apps.core.models import BaseModel


class ItemCompra(BaseModel):
    compra = ForeignKey('venda.Compra', verbose_name='Compra', on_delete=CASCADE)
    produto = ForeignKey('venda.Produto', verbose_name='Produto', on_delete=CASCADE)
    quantidade = PositiveIntegerField(verbose_name='Quantidade')
    valor_item = PositiveIntegerField(verbose_name='Valor Item', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Item Compra'
        verbose_name_plural = 'Itens Compra'

    def __str__(self):
        return self.produto.nome
    
    def save(self, *args, **kwargs):
        self.valor_item = float(self.produto.preco) * float(self.quantidade)
        super(ItemCompra, self).save(*args, **kwargs)
