# Generated by Django 4.1.4 on 2023-01-14 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "atendimento",
            "0003_alter_itemservico_options_itemconsulta_valor_item_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="itemconsulta",
            options={
                "ordering": ["-id"],
                "verbose_name": "Item de Consulta",
                "verbose_name_plural": "Itens de Consulta",
            },
        ),
        migrations.AlterModelOptions(
            name="tiposervico",
            options={
                "ordering": ["-id"],
                "verbose_name": "Tipo de Serviço",
                "verbose_name_plural": "Tipos de Serviços",
            },
        ),
    ]
