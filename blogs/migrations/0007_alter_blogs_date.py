# Generated by Django 4.2.9 on 2024-01-15 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_blogs_writer_name_alter_blogs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateField(default=datetime.date(2024, 1, 15)),
        ),
    ]