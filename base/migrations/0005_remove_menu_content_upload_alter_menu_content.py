# Generated by Django 4.1.7 on 2023-03-14 18:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_menu_content_upload"),
    ]

    operations = [
        migrations.RemoveField(model_name="menu", name="content_upload",),
        migrations.AlterField(
            model_name="menu",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]
