from django.db.models import ForeignKey, TextField, CASCADE, DateField, DecimalField
from apps.core.models import BaseModel
from django.db.models import Sum


class Consulta(BaseModel):
    pet = ForeignKey('core.Pet', verbose_name='Pet', on_delete=CASCADE)
    veterinario = ForeignKey('account.Veterinario', verbose_name='Veterinário', on_delete=CASCADE)
    sintomas = TextField(verbose_name='Sintomas')
    diagnostico = TextField(verbose_name='Diagnóstico')
    tratamento = TextField(verbose_name='Tratamento')
    data_consulta = DateField(verbose_name='Data da Consulta')
    valor_total = DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor Total')

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['-id']

    def __str__(self):
        return self.pet.nome

    @property
    def valor_consulta(self):
        print(dir(self))
        return self.itemconsulta_set.all().aggregate(valor_total=Sum('valor_item'))['valor_total'] + self.valor_total

