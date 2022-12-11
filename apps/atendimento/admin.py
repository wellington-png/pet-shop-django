from django.contrib.admin import ModelAdmin, register, TabularInline
from apps.atendimento.models import Consulta, ItemConsulta, TipoServico, Servico, ItemServico 


class ItemServicoInline(TabularInline):
    model = ItemServico
    extra = 1

class ItemConsultaInline(TabularInline):
    model = ItemConsulta
    extra = 1

@register(Consulta)
class ConsultaAdmin(ModelAdmin):
    inlines = [ItemConsultaInline]



@register(TipoServico)
class TipoServicoAdmin(ModelAdmin):
    pass

@register(Servico)
class ServicoAdmin(ModelAdmin):
    inlines = [ItemServicoInline]
