# Generated by Django 4.1 on 2022-08-14 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_order_complete_alter_order_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'آدرس حمل و نقل', 'verbose_name_plural': 'آدرس های حمل و نقل'},
        ),
    ]
