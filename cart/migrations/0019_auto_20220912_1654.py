# Generated by Django 3.2.15 on 2022-09-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0018_order_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='order',
            name='offline_method',
            field=models.BooleanField(default=False, verbose_name='پرداخت در محل'),
        ),
        migrations.AddField(
            model_name='order',
            name='online_method',
            field=models.BooleanField(default=True, verbose_name='پرداخت آنلاین'),
        ),
    ]
