# Generated by Django 5.0.6 on 2024-06-19 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_accountinformation_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinformation',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='سن کاربر'),
        ),
    ]
