# Generated by Django 5.1.2 on 2024-10-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_teammodel_description_ch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammodel',
            name='avatar',
            field=models.ImageField(default='assets/my/default.jpg', upload_to='team/', verbose_name='Avatar'),
        ),
    ]
