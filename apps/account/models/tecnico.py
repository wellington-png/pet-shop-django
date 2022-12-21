from django.db.models.fields import CharField
from apps.account.models import Funcionario


class Tecnico(Funcionario):
    crta = CharField(verbose_name='Crta', max_length=255)
