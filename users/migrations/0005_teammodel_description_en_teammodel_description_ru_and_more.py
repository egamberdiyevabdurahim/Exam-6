# Generated by Django 5.1.2 on 2024-10-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_teammodel_description_alter_teammodel_profession_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='teammodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='teammodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
    ]
