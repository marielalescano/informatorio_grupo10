# Generated by Django 3.0 on 2021-12-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20211219_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='avatar.png', upload_to='img_perfil'),
        ),
    ]
