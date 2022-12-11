from django.db.models import CharField

from apps.core.models import BaseModel

class Produto(BaseModel):
    nome = CharField(verbose_name='Nome', max_length=100)
    descricao = CharField(verbose_name='Descrição', max_length=100)
    preco = CharField(verbose_name='Preço', max_length=100)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome