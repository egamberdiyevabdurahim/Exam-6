# Generated by Django 5.1.2 on 2024-10-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_teammodel_description_zh_teammodel_profession_zh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammodel',
            old_name='description_zh',
            new_name='description_ch',
        ),
        migrations.RemoveField(
            model_name='teammodel',
            name='profession_zh',
        ),
        migrations.AddField(
            model_name='teammodel',
            name='profession_ch',
            field=models.CharField(max_length=128, null=True, verbose_name='Profession'),
        ),
    ]