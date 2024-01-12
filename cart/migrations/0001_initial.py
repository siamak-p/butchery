# Generated by Django 4.1 on 2022-08-14 07:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showmeat', '0005_meat_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت سفارش')),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره پیگیری')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='آدرس')),
                ('province', models.CharField(max_length=30, verbose_name='استان')),
                ('city', models.CharField(max_length=30, verbose_name='شهر')),
                ('zipcode', models.PositiveBigIntegerField(verbose_name='کد پستی')),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='لطفا شماره تماس را به صورت 09999999999 وارد فرمایید.', regex='^\\+?1?\\d{11}$')], verbose_name='شماره تماس')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usershipping', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordershipping', to='cart.order', verbose_name='سفارش')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='تعداد')),
                ('dated_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitem', to='cart.order', verbose_name='سفارش')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productitem', to='showmeat.meat', verbose_name='محصول')),
            ],
        ),
    ]
