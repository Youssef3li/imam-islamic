# Generated by Django 5.1.7 on 2025-04-05 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_article_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="created_at",
        ),
    ]
