from django.db.models import CharField, DecimalField
from apps.core.models import BaseModel


class TipoServico(BaseModel):
    descricao = CharField(verbose_name="Descrição", max_length=255)
    preco = DecimalField(verbose_name="Preço", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Tipo de Serviço"
        verbose_name_plural = "Tipos de Serviços"
        ordering = ["-id"]

    def __str__(self):
        return self.descricao
