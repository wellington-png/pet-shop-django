# Generated by Django 4.1.4 on 2022-12-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("venda", "0003_alter_compra_options_alter_compra_valor_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="compra",
            name="data_compra",
            field=models.DateField(
                blank=True, null=True, verbose_name="Data da Compra"
            ),
        ),
    ]
