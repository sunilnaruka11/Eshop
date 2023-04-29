# Generated by Django 4.2 on 2023-04-06 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.IntegerField(default=0)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=200, null=True),
                ),
                ("image", models.ImageField(upload_to="uploads/products/")),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.category",
                    ),
                ),
            ],
        ),
    ]