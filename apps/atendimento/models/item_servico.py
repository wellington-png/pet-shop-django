from django.db.models import ForeignKey, CASCADE, PositiveIntegerField
from apps.core.models import BaseModel


class ItemServico(BaseModel):
    servico = ForeignKey(
        "atendimento.Servico", verbose_name="Serviço", on_delete=CASCADE
    )
    tipo_servico = ForeignKey(
        "atendimento.TipoServico", verbose_name="Tipo de Serviço", on_delete=CASCADE
    )
    quantidade = PositiveIntegerField(verbose_name="Quantidade")
    valor_item = PositiveIntegerField(verbose_name="Valor Item", blank=True, null=True)

    class Meta:
        verbose_name = "Item de Serviço"
        verbose_name_plural = "Itens de Serviço"
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        self.valor_item = float(self.tipo_servico.preco) * float(self.quantidade)
        super(ItemServico, self).save(*args, **kwargs)

    def __str__(self):
        return self.servico.pet.nome
