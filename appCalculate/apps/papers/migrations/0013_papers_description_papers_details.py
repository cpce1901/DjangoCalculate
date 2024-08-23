# Generated by Django 5.0.7 on 2024-08-23 14:34

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0012_remove_papers_description_remove_papers_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='description',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name='Desarrollo'),
        ),
        migrations.AddField(
            model_name='papers',
            name='details',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name='Reseña'),
        ),
    ]
