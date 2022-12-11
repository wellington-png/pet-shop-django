# Generated by Django 4.1.4 on 2022-12-10 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "valor_total",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Valor Total"
                    ),
                ),
                (
                    "atendente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.atendente",
                        verbose_name="Atendente",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.cliente",
                        verbose_name="Cliente",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "descricao",
                    models.CharField(max_length=100, verbose_name="Descrição"),
                ),
                ("preco", models.CharField(max_length=100, verbose_name="Preço")),
            ],
            options={
                "verbose_name": "Produto",
                "verbose_name_plural": "Produtos",
            },
        ),
        migrations.CreateModel(
            name="ItemCompra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("quantidade", models.PositiveIntegerField(verbose_name="Quantidade")),
                (
                    "compra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="venda.compra",
                        verbose_name="Compra",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="venda.produto",
                        verbose_name="Produto",
                    ),
                ),
            ],
            options={
                "verbose_name": "Item Compra",
                "verbose_name_plural": "Itens Compra",
            },
        ),
        migrations.CreateModel(
            name="Estoque",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("quantidade", models.PositiveIntegerField(verbose_name="Quantidade")),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="venda.produto",
                        verbose_name="Produto",
                    ),
                ),
            ],
            options={
                "verbose_name": "Estoque",
                "verbose_name_plural": "Estoque",
            },
        ),
    ]
