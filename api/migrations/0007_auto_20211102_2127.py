# Generated by Django 3.1.8 on 2021-11-02 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211102_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Advisor_id',
            new_name='advisor',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='User_id',
            new_name='user',
        ),
    ]
