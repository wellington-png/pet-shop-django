# Generated by Django 4.1.4 on 2023-01-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("atendimento", "0002_alter_consulta_options_alter_servico_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="itemservico",
            options={
                "ordering": ["-id"],
                "verbose_name": "Item de Serviço",
                "verbose_name_plural": "Itens de Serviço",
            },
        ),
        migrations.AddField(
            model_name="itemconsulta",
            name="valor_item",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Valor Item"
            ),
        ),
        migrations.AddField(
            model_name="itemservico",
            name="valor_item",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Valor Item"
            ),
        ),
    ]
