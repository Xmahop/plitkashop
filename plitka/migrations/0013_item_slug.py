# Generated by Django 2.2 on 2019-05-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plitka', '0012_category_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.CharField(default=None, max_length=150, verbose_name='Ссылка'),
        ),
    ]