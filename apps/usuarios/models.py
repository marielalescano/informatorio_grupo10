from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    email = models.EmailField(max_length= 254, null= False)
    imagen_perfil= models.ImageField(upload_to = 'imagenes_post', default = 'avatar.png')


    class Meta:

        verbose_name = 'Usuario'
        verbose_name_plural ='Usuarios'


    def __str__(self):

        return self.username