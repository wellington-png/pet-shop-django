from django.db.models import ForeignKey, CASCADE, PositiveIntegerField

from apps.core.models import BaseModel


class Estoque(BaseModel):
    produto = ForeignKey("venda.Produto", verbose_name="Produto", on_delete=CASCADE)
    quantidade = PositiveIntegerField(verbose_name="Quantidade")

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoque"
        ordering = ["-id"]

    def __str__(self):
        return self.produto.nome
