# Generated by Django 5.0.6 on 2024-06-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinformation',
            name='access_level',
            field=models.CharField(choices=[('R', 'فقط خواندن'), ('R_W', 'خواندن و نوشتن')], default='R', max_length=20, verbose_name='مشخص کردن سطح دسترسی'),
        ),
        migrations.AlterField(
            model_name='accountinformation',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='تلفن'),
        ),
    ]
