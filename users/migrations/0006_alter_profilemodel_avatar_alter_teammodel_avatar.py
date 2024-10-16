# Generated by Django 5.1.2 on 2024-10-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_teammodel_description_en_teammodel_description_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='users/', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='team/', verbose_name='Avatar'),
        ),
    ]
