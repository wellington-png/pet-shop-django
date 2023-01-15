# Generated by Django 4.1.4 on 2023-01-15 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("atendimento", "0004_alter_itemconsulta_options_alter_tiposervico_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consulta",
            name="valor_total",
            field=models.DecimalField(
                decimal_places=2, max_digits=18, verbose_name="Valor Total"
            ),
        ),
        migrations.AlterField(
            model_name="servico",
            name="valor_total",
            field=models.DecimalField(
                decimal_places=2, max_digits=18, verbose_name="Valor Total"
            ),
        ),
    ]
