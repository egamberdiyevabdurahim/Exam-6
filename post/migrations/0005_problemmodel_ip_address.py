# Generated by Django 5.1.2 on 2024-10-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_offermodel_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemmodel',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
