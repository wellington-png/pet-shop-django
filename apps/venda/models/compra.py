from django.db.models import ForeignKey, CASCADE, DecimalField, DateField
from apps.core.models import BaseModel
from django.utils.timezone import now
from django.db.models import Sum

class Compra(BaseModel):
    cliente = ForeignKey('core.Cliente', verbose_name='Cliente', on_delete=CASCADE)
    atendente = ForeignKey('account.Atendente', verbose_name='Atendente', on_delete=CASCADE)
    data_compra = DateField(verbose_name='Data da Compra', blank=True, null=True, auto_now_add=True)
    valor_total = DecimalField(verbose_name='Valor Total', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cliente.nome

    @property
    def valor(self):
        t = self.itemcompra_set.aggregate(Sum('valor_item'))['valor_item__sum'] or 0
        self.valor_total = t
        self.save()
        return f'R$ {t}'

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['-id']
        

