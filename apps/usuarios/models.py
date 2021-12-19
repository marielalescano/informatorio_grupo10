from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    website = models.URLField(max_length=200, blank=True)

    photo = models.ImageField(upload_to='img_perfil',default = 'media/avatar.png')

    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        
        return self.user.username




