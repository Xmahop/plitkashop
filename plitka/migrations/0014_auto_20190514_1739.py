# Generated by Django 2.2 on 2019-05-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plitka', '0013_item_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
        migrations.AddField(
            model_name='item',
            name='count',
            field=models.CharField(default=None, max_length=150, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(default=None, max_length=150, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(default=None, max_length=150, verbose_name='Описание'),
        ),
    ]
