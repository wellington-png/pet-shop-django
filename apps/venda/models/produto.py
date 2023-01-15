from django.db.models import CharField, DecimalField, TextField
from stdimage import StdImageField

from apps.core.models import BaseModel


class Produto(BaseModel):
    nome = CharField(verbose_name="Nome", max_length=100)
    descricao = TextField(verbose_name="Descrição")
    preco = DecimalField(verbose_name="Preço", max_digits=10, decimal_places=2)
    imagem = StdImageField(
        verbose_name="Imagem",
        upload_to="produtos",
        variations={
            "miniatura": {"width": 100, "height": 100, "crop": True},
            "thumbnail": {"width": 480, "height": 480, "crop": True},
        },
        default="produtos/default.jpg",
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["-id"]

    def __str__(self):
        return self.nome
