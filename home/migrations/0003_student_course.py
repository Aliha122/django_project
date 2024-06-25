# Generated by Django 5.0.6 on 2024-06-17 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_person_email_person_hb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دانش آموز')),
                ('familly', models.CharField(max_length=100, verbose_name='نام  خانوادگی دانش آموز')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام درس')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person', verbose_name='معلم')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student', verbose_name='دانش آموز')),
            ],
        ),
    ]