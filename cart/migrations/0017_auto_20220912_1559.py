# Generated by Django 3.2.15 on 2022-09-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_auto_20220912_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_day',
            field=models.CharField(default=0, max_length=30, verbose_name='روز ارسال'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.CharField(default=0, max_length=10, verbose_name='زمان ارسال'),
        ),
    ]
