from django.db.models import ForeignKey, CASCADE, PositiveIntegerField
from apps.core.models import BaseModel


class ItemConsulta(BaseModel):
    consulta = ForeignKey('atendimento.Consulta', verbose_name='Consulta', on_delete=CASCADE)
    tipo_servico = ForeignKey('atendimento.TipoServico', verbose_name='Tipo de Serviço', on_delete=CASCADE)
    quantidade = PositiveIntegerField(verbose_name='Quantidade')

    class Meta:
        verbose_name = 'Item de Consulta'
        verbose_name_plural = 'Itens de Consulta'

    def __str__(self):
        return self.consulta.pet.nome