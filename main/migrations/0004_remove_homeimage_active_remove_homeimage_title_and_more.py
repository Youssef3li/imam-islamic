# Generated by Django 5.1.7 on 2025-04-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homeimage",
            name="active",
        ),
        migrations.RemoveField(
            model_name="homeimage",
            name="title",
        ),
        migrations.AlterField(
            model_name="homeimage",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="home_images/"),
        ),
    ]
