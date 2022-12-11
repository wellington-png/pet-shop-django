from django.contrib.admin import ModelAdmin, register
from apps.core.models import Cliente, Pet


@register(Cliente)
class ClienteAdmin(ModelAdmin):
    pass
    list_display = (
        "cpf",
        "nome",
        "logradoro",
        "cidade",
        "uf",
        "cep",
        "contato",
    )
    search_fields = (
        "cpf",
        "nome",
        "logradoro",
        "cidade",
        "uf",
        "cep",
        "contato",
    )
    list_filter = (
        "cpf",
        "nome",
        "logradoro",
        "cidade",
        "uf",
        "cep",
        "contato",
    )


@register(Pet)
class PetAdmin(ModelAdmin):
    pass
    list_display = (
        "nome",
        "raca",
        "peso",
        "data_nascimento",
        "sexo",
        "especie",
        "porte",
        "pelagem",
        "cliente",
    )
    search_fields = (
        "nome",
        "raca",
        "peso",
        "data_nascimento",
        "sexo",
        "especie",
        "porte",
        "pelagem",
        "cliente",
    )
    list_filter = (
        "nome",
        "raca",
        "peso",
        "data_nascimento",
        "sexo",
        "especie",
        "porte",
        "pelagem",
        "cliente",
    )
