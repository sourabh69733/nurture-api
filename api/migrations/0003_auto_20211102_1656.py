# Generated by Django 3.1.8 on 2021-11-02 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211102_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 16, 56, 3, 432597)),
        ),
    ]
