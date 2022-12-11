from django.db.models import CharField
from apps.account.models import Funcionario


class Atendente(Funcionario):
    cra = CharField(verbose_name='CRA', max_length=255)


    def save(self, *args, **kwargs):
        self.fucionario_type = 'atendente'
        super(Atendente, self).save(*args, **kwargs)