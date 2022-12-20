from django.db.models import ForeignKey, CASCADE, DecimalField, DateField

from apps.core.models import BaseModel
from django.utils.timezone import now

class Compra(BaseModel):
    cliente = ForeignKey('core.Cliente', verbose_name='Cliente', on_delete=CASCADE)
    atendente = ForeignKey('account.Atendente', verbose_name='Atendente', on_delete=CASCADE)
    valor_total = DecimalField(verbose_name='Valor Total', max_digits=10, decimal_places=2)
    data_compra = DateField(verbose_name='Data da Compra', blank=True, null=True)

    def __str__(self):
        return self.cliente.nome

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['-data_compra']