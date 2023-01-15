# Generated by Django 4.1.4 on 2023-01-14 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="atendente",
            options={
                "ordering": ["-id"],
                "verbose_name": "Atendente",
                "verbose_name_plural": "Atendentes",
            },
        ),
        migrations.AlterModelOptions(
            name="funcionario",
            options={
                "ordering": ["-id"],
                "verbose_name": "usuário",
                "verbose_name_plural": "usuários",
            },
        ),
        migrations.AlterModelOptions(
            name="tecnico",
            options={
                "ordering": ["-id"],
                "verbose_name": "Técnico",
                "verbose_name_plural": "Técnicos",
            },
        ),
        migrations.AlterModelOptions(
            name="veterinario",
            options={
                "ordering": ["-id"],
                "verbose_name": "Veterinário",
                "verbose_name_plural": "Veterinários",
            },
        ),
    ]