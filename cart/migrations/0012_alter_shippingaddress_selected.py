# Generated by Django 3.2.15 on 2022-09-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_alter_shippingaddress_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='selected',
            field=models.BooleanField(default=False, verbose_name='آدرس منتخب'),
        ),
    ]
