# Generated by Django 3.0 on 2021-12-18 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20211218_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='usuario',
            new_name='user',
        ),
    ]