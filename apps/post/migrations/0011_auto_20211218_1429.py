# Generated by Django 3.0 on 2021-12-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]