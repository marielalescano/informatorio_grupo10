from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoría', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Categoría Activada/Categoría no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de creación',auto_now=False, auto_now_add= True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural ='Categorías'

    def __str__(self):
        return self.nombre


class Post(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField('Título', max_length=100,null=False,blank=False)
    slug=models.CharField('slug', max_length=100,null=False,blank=False)
    descripcion=models.CharField('Descripción', max_length= 110,null=False,blank=False)
    contenido=RichTextField()
    imagen=models.URLField(max_length=270, null=False,blank=False)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.titulo