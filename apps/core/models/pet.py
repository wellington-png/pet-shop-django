from django.db.models import CharField, DecimalField, DateTimeField, ForeignKey, CASCADE

from apps.core.models import BaseModel


class Pet(BaseModel):
    nome = CharField(max_length=255, verbose_name='Nome')
    raca = CharField(max_length=255, verbose_name='Raça')
    peso = DecimalField(max_digits=5, decimal_places=2, verbose_name='Peso')
    data_nascimento = DateTimeField(verbose_name='Data de Nascimento', null=True, blank=True)
    sexo = CharField(max_length=255, verbose_name='Sexo')
    especie = CharField(max_length=255, verbose_name='Espécie')
    porte = CharField(max_length=255, verbose_name='Porte')
    pelagem = CharField(max_length=255, verbose_name='Pelagem')
    cliente = ForeignKey('Cliente', on_delete=CASCADE, verbose_name='Cliente')


    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return self.nome