# Generated by Django 5.1.7 on 2025-04-02 17:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_article_image_alter_article_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
