# Generated by Django 3.2.15 on 2022-09-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='کد پستی'),
        ),
    ]
