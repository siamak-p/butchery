# Generated by Django 4.1 on 2022-08-14 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سفارش', 'verbose_name_plural': 'سفارشات'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'محصول سفارش داده شده', 'verbose_name_plural': 'محصولات سفارش داده شده'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'آدرس خمل و نقل', 'verbose_name_plural': 'آدرس های حمل و نقل'},
        ),
    ]
