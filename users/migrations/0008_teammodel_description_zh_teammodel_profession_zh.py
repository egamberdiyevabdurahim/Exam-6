# Generated by Django 5.1.2 on 2024-10-12 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profilemodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammodel',
            name='description_zh',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='teammodel',
            name='profession_zh',
            field=models.CharField(max_length=128, null=True, verbose_name='Profession'),
        ),
    ]
