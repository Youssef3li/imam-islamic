# Generated by Django 5.1.7 on 2025-04-11 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_slider"),
    ]

    operations = [
        migrations.CreateModel(
            name="Advertisement",
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
                ("image", models.ImageField(blank=True, null=True, upload_to="ads/")),
                ("link", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
