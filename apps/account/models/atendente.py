from django.db.models import CharField
from apps.account.models import Funcionario


class Atendente(Funcionario):
    cra = CharField(verbose_name="CRA", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Atendente"
        verbose_name_plural = "Atendentes"
        ordering = ["-id"]
