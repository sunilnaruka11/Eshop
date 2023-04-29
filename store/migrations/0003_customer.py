# Generated by Django 4.2 on 2023-04-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=500)),
            ],
        ),
    ]
