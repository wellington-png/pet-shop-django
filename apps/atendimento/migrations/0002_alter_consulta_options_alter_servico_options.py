# Generated by Django 4.1.4 on 2023-01-07 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("atendimento", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="consulta",
            options={
                "ordering": ["-id"],
                "verbose_name": "Consulta",
                "verbose_name_plural": "Consultas",
            },
        ),
        migrations.AlterModelOptions(
            name="servico",
            options={
                "ordering": ["-id"],
                "verbose_name": "Serviço",
                "verbose_name_plural": "Serviços",
            },
        ),
    ]
