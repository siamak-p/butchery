# Generated by Django 3.2.15 on 2022-09-30 12:41

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0026_alter_order_online_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_time',
        ),
        migrations.AlterField(
            model_name='deliverytimemodel',
            name='day',
            field=django_jalali.db.models.jDateField(default=datetime.date(2022, 9, 30), max_length=30, verbose_name='روز ارسال'),
        ),
        migrations.AlterField(
            model_name='deliverytimemodel',
            name='flags',
            field=django_jalali.db.models.jDateField(default=datetime.date(2022, 10, 1), max_length=30, verbose_name='فردا'),
        ),
    ]
