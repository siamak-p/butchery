# Generated by Django 3.2.15 on 2022-10-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0031_auto_20221011_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemhistory',
            name='delivery_day',
        ),
        migrations.RemoveField(
            model_name='orderitemhistory',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='orderitemhistory',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderitemhistory',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='npzexx28wr2wrvo', max_length=50, verbose_name='شماره پیگیری'),
        ),
    ]