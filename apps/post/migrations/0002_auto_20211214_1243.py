# Generated by Django 3.0 on 2021-12-14 15:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del objetivo')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes_post')),
                ('estado', models.BooleanField(default=True, verbose_name='Objetivo Activado/No Activado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Objetivo',
                'verbose_name_plural': 'Objetivos',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('descripcion', models.CharField(max_length=110, verbose_name='Descripción')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(null=True, upload_to='imagenes_post')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('objetivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Objetivo')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
