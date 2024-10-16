# Generated by Django 5.1.2 on 2024-10-12 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_aboutmodel_description_ru_aboutmodel_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='description_zh',
            field=models.TextField(null=True, verbose_name='About Description'),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='title_zh',
            field=models.CharField(max_length=128, null=True, verbose_name='About Title'),
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='answer_zh',
            field=models.TextField(null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='question_zh',
            field=models.CharField(max_length=128, null=True, verbose_name='Question'),
        ),
    ]
