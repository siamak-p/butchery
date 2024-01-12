# Generated by Django 3.2.18 on 2023-05-11 15:42

import datetime
from django.db import migrations, models
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0037_auto_20221105_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemhistory',
            name='addedtime',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ثبت سفارش'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliverytimemodel',
            name='day',
            field=django_jalali.db.models.jDateField(default=datetime.date(2023, 5, 11), max_length=30, verbose_name='روز ارسال'),
        ),
        migrations.AlterField(
            model_name='deliverytimemodel',
            name='flags',
            field=django_jalali.db.models.jDateField(default=datetime.date(2023, 5, 12), max_length=30, verbose_name='فردا'),
        ),
    ]
