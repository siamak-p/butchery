# Generated by Django 3.2.15 on 2022-09-29 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_remove_orderitemhistory_delivery_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_time',
            new_name='delivery_time_bound',
        ),
    ]