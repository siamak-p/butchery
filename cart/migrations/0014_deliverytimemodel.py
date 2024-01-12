# Generated by Django 3.1 on 2022-09-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_auto_20220911_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryTimeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=('1401', 'شهریور', '20'), verbose_name='روز ارسال')),
                ('time1', models.BooleanField(default=True, verbose_name='زمان ارسال تام اول')),
                ('time1_flag', models.PositiveSmallIntegerField(default=10, verbose_name='کنترلر تایم اول')),
                ('time2', models.BooleanField(default=True, verbose_name='زمان ارسال تایم دوم')),
                ('time2_flag', models.PositiveSmallIntegerField(default=10, verbose_name='کنترلر تایم دوم')),
                ('time3', models.BooleanField(default=True, verbose_name='زمان ارسال تایم سوم')),
                ('time3_flag', models.PositiveSmallIntegerField(default=10, verbose_name='کنترلر تایم سوم')),
                ('time4', models.BooleanField(default=True, verbose_name='زمان ارسال تایم سوم')),
                ('time4_flag', models.PositiveSmallIntegerField(default=10, verbose_name='کنترلر تایم چهارم')),
                ('flags', models.CharField(default=('1401', 'شهریور', 21), max_length=30, verbose_name='فردا')),
            ],
            options={
                'verbose_name': 'زمان ارسال',
                'verbose_name_plural': 'زمانهای ارسال',
            },
        ),
    ]
