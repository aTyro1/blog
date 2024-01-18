# Generated by Django 4.2.9 on 2024-01-09 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(default='Title of the Article!<GENERATED by SYSTEM>', max_length=200)),
                ('blog', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='verified_writer',
            fields=[
                ('writer_name', models.CharField(max_length=30)),
                ('writer_id', models.CharField(default='', max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_name', models.CharField(max_length=30)),
                ('writer_id', models.CharField(default='', max_length=30)),
            ],
        ),
    ]