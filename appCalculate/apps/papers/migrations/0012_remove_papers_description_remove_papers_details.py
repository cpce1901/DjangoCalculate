# Generated by Django 5.0.7 on 2024-08-23 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0011_papers_description_papers_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='papers',
            name='description',
        ),
        migrations.RemoveField(
            model_name='papers',
            name='details',
        ),
    ]
