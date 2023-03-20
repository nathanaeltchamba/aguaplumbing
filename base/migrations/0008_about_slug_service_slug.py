# Generated by Django 4.1.7 on 2023-03-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_alter_menu_snippet_service_about"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="slug",
            field=models.SlugField(default="new-slug", unique=True),
        ),
        migrations.AddField(
            model_name="service",
            name="slug",
            field=models.SlugField(default="new-slug", unique=True),
        ),
    ]
