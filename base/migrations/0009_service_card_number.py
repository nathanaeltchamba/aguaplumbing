# Generated by Django 4.1.7 on 2023-03-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_about_slug_service_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="card_number",
            field=models.IntegerField(default=0),
        ),
    ]
