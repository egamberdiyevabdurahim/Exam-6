# Generated by Django 5.1.2 on 2024-10-12 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_description_zh_teammodel_description_ch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammodel',
            name='description_ch',
        ),
        migrations.RemoveField(
            model_name='teammodel',
            name='profession_ch',
        ),
    ]
