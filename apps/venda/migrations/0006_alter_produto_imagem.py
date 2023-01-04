# Generated by Django 4.1.4 on 2022-12-31 21:03

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ("venda", "0005_produto_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="imagem",
            field=stdimage.models.StdImageField(
                default="produtos/default.jpg",
                force_min_size=False,
                upload_to="produtos",
                variations={
                    "miniatura": {"crop": True, "height": 100, "width": 100},
                    "thumbnail": {"crop": True, "height": 480, "width": 480},
                },
                verbose_name="Imagem",
            ),
        ),
    ]
