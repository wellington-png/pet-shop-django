from django.db.models import ForeignKey, CASCADE, DateField, DecimalField
from django.db.models.signals import post_delete
from django.db.models import  Sum
import datetime
from apps.core.models import BaseModel



class Servico(BaseModel):
    pet = ForeignKey('core.Pet', verbose_name='Pet', on_delete=CASCADE)
    tecnico = ForeignKey('account.Tecnico', verbose_name='Técnico', on_delete=CASCADE)
    data_servico = DateField(verbose_name='Data do Serviço')
    valor_total = DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor Total')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['-data_servico']

    def __str__(self):
        return self.pet.nome
    

def pre_save_servico(sender, instance, **kwargs):
    instance.data_servico = datetime.now()
    instance.valor_total = instance.item_servico_set.aggregate(Sum('preco') *  Sum('quantidade'))
    print(instance.valor_total)
    instance.save()

post_delete.connect(pre_save_servico, sender=Servico)
    
    