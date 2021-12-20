from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    website = models.URLField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='img_perfil',default = 'avatar.png')
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):        
        return self.user.username

# Esta función hace que al registrarse y crearse un usuario se cree también el Profile

def crear_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(crear_profile, sender=User)




