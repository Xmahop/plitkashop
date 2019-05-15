# Generated by Django 2.2 on 2019-05-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plitka', '0009_auto_20190429_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(choices=[('trotuar', 'Тротуарная плитка'), ('vibrolit', 'Вибролитьевая плитка'), ('vibropress', 'Вибропресованная плитка')], verbose_name='Slug'),
        ),
    ]