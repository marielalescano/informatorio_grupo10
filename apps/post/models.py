from django.db import models

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
