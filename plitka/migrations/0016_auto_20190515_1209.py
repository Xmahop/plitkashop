# Generated by Django 2.2 on 2019-05-15 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plitka', '0015_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=None, max_length=500, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.ImageField(default=None, upload_to='category'),
        ),
    ]
