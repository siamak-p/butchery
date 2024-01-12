# Generated by Django 3.2.15 on 2022-11-05 10:28

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0036_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverytimemodel',
            name='day',
            field=django_jalali.db.models.jDateField(default=datetime.date(2022, 11, 5), max_length=30, verbose_name='روز ارسال'),
        ),
        migrations.AlterField(
            model_name='deliverytimemodel',
            name='flags',
            field=django_jalali.db.models.jDateField(default=datetime.date(2022, 11, 6), max_length=30, verbose_name='فردا'),
        ),
    ]