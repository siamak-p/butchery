# Generated by Django 4.0.5 on 2022-06-28 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showmeat', '0002_meat_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندیها'},
        ),
        migrations.AlterModelOptions(
            name='meat',
            options={'verbose_name': 'گوشت', 'verbose_name_plural': 'گوشتها'},
        ),
    ]
