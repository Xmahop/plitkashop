# Generated by Django 2.2 on 2019-04-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plitka', '0003_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default=None, upload_to='media/'),
        ),
    ]
