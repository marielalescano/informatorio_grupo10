from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User




class Objetivo(models.Model):
    nombre = models.CharField('Nombre del objetivo', max_length = 100, null = False, blank = False)
    descripcion = models.TextField('Descripción', null=False)
    imagen=models.ImageField(upload_to = 'imagenes_post', null = True)
    estado = models.BooleanField('Objetivo Activado/No Activado', default = True)
    fecha_creacion = models.DateField('Fecha de creación',auto_now=False, auto_now_add= True)

    class Meta:
        verbose_name = 'Objetivo'
        verbose_name_plural ='Objetivos'

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo=models.CharField('Título', max_length=100,null=False,blank=False)
    descripcion=models.CharField('Descripción', max_length= 110,null=False,blank=False)
    contenido=RichTextField()
    imagen=models.ImageField(upload_to = 'imagenes_post', null = True)
    objetivo = models.ForeignKey(Objetivo, on_delete = models.CASCADE, null=False)
    estado = models.BooleanField('Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name = 'post_likes')  

    def cantidad_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'


    def __str__(self):
        return self.titulo