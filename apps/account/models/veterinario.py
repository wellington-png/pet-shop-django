from django.db.models import CharField
from apps.account.models import Funcionario


class Veterinario(Funcionario):
    crmv = CharField(verbose_name='CRMV', max_length=255)

    def save(self, *args, **kwargs):
        self.fucionario_type = 'veterinario'
        super(Veterinario, self).save(*args, **kwargs)
