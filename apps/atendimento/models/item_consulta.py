from django.db.models import ForeignKey, CASCADE, PositiveIntegerField
from apps.core.models import BaseModel


class ItemConsulta(BaseModel):
    consulta = ForeignKey('atendimento.Consulta', verbose_name='Consulta', on_delete=CASCADE)
    tipo_servico = ForeignKey('atendimento.TipoServico', verbose_name='Tipo de Serviço', on_delete=CASCADE)
    quantidade = PositiveIntegerField(verbose_name='Quantidade')
    valor_item = PositiveIntegerField(verbose_name='Valor Item', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Item de Consulta'
        verbose_name_plural = 'Itens de Consulta'
        ordering = ["-id"]
        
    def save(self, *args, **kwargs):
        self.valor_item = float(self.tipo_servico.preco) * float(self.quantidade)
        super(ItemConsulta, self).save(*args, **kwargs)

    def __str__(self):
        return self.consulta.pet.nome