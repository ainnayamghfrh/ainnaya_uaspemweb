# Generated by Django 5.0.3 on 2024-06-23 04:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0006_artikel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
