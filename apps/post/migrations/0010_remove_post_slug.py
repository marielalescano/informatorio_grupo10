# Generated by Django 3.0 on 2021-12-18 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20211217_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
