# Generated by Django 3.2.15 on 2022-09-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0027_auto_20220930_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemhistory',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره پیگیری'),
        ),
    ]
