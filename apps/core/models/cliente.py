from django.db.models import CharField

from apps.core.models import BaseModel


class Cliente(BaseModel):
    cpf = CharField(max_length=255, verbose_name='CPF')
    nome = CharField(max_length=255, verbose_name='Nome')
    logradoro = CharField(max_length=255, verbose_name='Logradoro')
    cidade = CharField(max_length=255, verbose_name='Cidade')
    uf = CharField(max_length=255, verbose_name='UF')
    cep = CharField(max_length=255, verbose_name='CEP')
    contato = CharField(max_length=255, verbose_name='Contato')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'