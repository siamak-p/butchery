# Generated by Django 3.2.15 on 2022-09-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_shippingaddress_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='کد پستی'),
        ),
    ]
