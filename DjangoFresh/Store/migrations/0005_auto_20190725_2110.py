# Generated by Django 2.1.8 on 2019-07-25 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_auto_20190725_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodstype',
            old_name='descripyion',
            new_name='description',
        ),
    ]