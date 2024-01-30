# Generated by Django 5.0.1 on 2024-01-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0003_writer_writer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='users/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
