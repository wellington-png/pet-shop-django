from django.db.models import ForeignKey, CASCADE, PositiveIntegerField
from apps.core.models import BaseModel


class ItemServico(BaseModel):
    servico = ForeignKey('atendimento.Servico', verbose_name='Serviço', on_delete=CASCADE)
    tipo_servico = ForeignKey('atendimento.TipoServico', verbose_name='Tipo de Serviço', on_delete=CASCADE)
    quantidade = PositiveIntegerField(verbose_name='Quantidade')

    class Meta:
        verbose_name = 'Item de Serviço'
        verbose_name_plural = 'Itens de Serviço'

    def __str__(self):
        return self.servico.pet.nome
