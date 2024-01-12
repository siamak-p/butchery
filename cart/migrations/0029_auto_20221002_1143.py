# Generated by Django 3.2.15 on 2022-10-02 08:13

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0028_orderitemhistory_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverytimemodel',
            name='day',
            field=django_jalali.db.models.jDateField(default=datetime.date(2022, 10, 2), max_length=30, verbose_name='روز ارسال'),
        ),
        migrations.AlterField(
            model_name='deliverytimemodel',
            name='flags',
            field=django_jalali.db.models.jDateField(default=datetime.date(2022, 10, 3), max_length=30, verbose_name='فردا'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='gviwub7epvi6kl2', max_length=50, verbose_name='شماره پیگیری'),
        ),
    ]
