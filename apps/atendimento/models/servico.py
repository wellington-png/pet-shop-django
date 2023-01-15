from django.db.models import ForeignKey, CASCADE, DateField, DecimalField
from apps.core.models import BaseModel
from django.db.models import Sum


class Servico(BaseModel):
    pet = ForeignKey('core.Pet', verbose_name='Pet', on_delete=CASCADE)
    tecnico = ForeignKey('account.Tecnico', verbose_name='Técnico', on_delete=CASCADE)
    data_servico = DateField(verbose_name='Data do Serviço')
    valor_total = DecimalField(max_digits=18, decimal_places=2, verbose_name='Valor Total')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['-id']

    def __str__(self):
        return self.pet.nome

    @property
    def valor_servico(self):
        return self.itemservico_set.all().aggregate(valor_total=Sum('valor_item'))['valor_total'] + self.valor_total
        