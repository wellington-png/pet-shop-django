from django.db.models import CharField
from apps.account.models import Funcionario


class Veterinario(Funcionario):
    crmv = CharField(verbose_name='CRMV', max_length=255)
