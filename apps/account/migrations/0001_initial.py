# Generated by Django 4.1.4 on 2022-12-10 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Funcionario",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="nome completo"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="endereço de e-mail"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Username"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="status de admin"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="ativo")),
                (
                    "fucionario_type",
                    models.CharField(
                        default="funcionario", max_length=255, verbose_name="tipo"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "usuário",
                "verbose_name_plural": "usuários",
                "ordering": ["name", "created_at"],
            },
        ),
        migrations.CreateModel(
            name="Atendente",
            fields=[
                (
                    "funcionario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("cra", models.CharField(max_length=255, verbose_name="CRA")),
            ],
            options={
                "abstract": False,
            },
            bases=("account.funcionario",),
        ),
        migrations.CreateModel(
            name="Tecnico",
            fields=[
                (
                    "funcionario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("crta", models.CharField(max_length=255, verbose_name="Crta")),
            ],
            options={
                "abstract": False,
            },
            bases=("account.funcionario",),
        ),
        migrations.CreateModel(
            name="Veterinario",
            fields=[
                (
                    "funcionario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("crmv", models.CharField(max_length=255, verbose_name="CRMV")),
            ],
            options={
                "abstract": False,
            },
            bases=("account.funcionario",),
        ),
    ]
