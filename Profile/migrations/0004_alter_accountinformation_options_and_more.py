# Generated by Django 5.0.6 on 2024-06-20 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_accountinformation_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountinformation',
            options={'verbose_name_plural': 'حساب کاربری'},
        ),
        migrations.AlterModelTable(
            name='accountinformation',
            table='AccountInformation',
        ),
    ]
