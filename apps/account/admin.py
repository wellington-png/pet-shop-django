from django.contrib.admin import ModelAdmin, register
from apps.account.models import Atendente, Funcionario, Tecnico, Veterinario
from apps.account.forms import (
    UserDashCreationForm,
    VeterinarioForm,
    TecnicoForm,
    AtendenteForm,
)


@register(Atendente)
class AtendenteAdmin(ModelAdmin):
    model = Atendente
    list_display = ["username", "email", "name", "is_staff", "is_active"]
    search_fields = ["username", "email", "name"]
    form = AtendenteForm


@register(Funcionario)
class FuncionarioAdmin(ModelAdmin):
    model = Funcionario
    list_display = ["username", "email", "name", "is_staff", "is_active"]
    search_fields = ["username", "email", "name"]
    form = UserDashCreationForm


@register(Tecnico)
class TecnicoAdmin(ModelAdmin):
    model = Tecnico
    list_display = ["username", "email", "name", "is_staff", "is_active"]
    search_fields = ["username", "email", "name"]
    form = TecnicoForm


@register(Veterinario)
class VeterinarioAdmin(ModelAdmin):
    model = Veterinario
    list_display = ["username", "email", "name", "is_staff", "is_active"]
    search_fields = ["username", "email", "name"]
    form = VeterinarioForm
