# Generated by Django 5.1.2 on 2024-10-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_teammodel_first_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammodel',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='profession',
            field=models.CharField(max_length=128, verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='profession_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='profession_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='profession_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='Profession'),
        ),
    ]
