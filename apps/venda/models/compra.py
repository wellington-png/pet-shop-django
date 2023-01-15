from django.db.models import ForeignKey, CASCADE, DecimalField, DateField
from apps.core.models import BaseModel
from django.utils.timezone import now
from django.db.models import Sum


class Compra(BaseModel):
    cliente = ForeignKey("core.Cliente", verbose_name="Cliente", on_delete=CASCADE)
    atendente = ForeignKey(
        "account.Atendente", verbose_name="Atendente", on_delete=CASCADE
    )
    data_compra = DateField(verbose_name="Data da Compra", blank=True, null=True)

    def __str__(self):
        return self.cliente.nome

    @property
    def valor_total(self):
        valor = (
            self.itemcompra_set.all().aggregate(Sum("valor_item"))["valor_item__sum"]
            or 0
        )
        return "R$ {}".format(valor)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ["-id"]
