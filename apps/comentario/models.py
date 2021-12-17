from django.db import models
from django.contrib.auth.models import User
from apps.post.models import Post


class Comment(models.Model):
     
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    #profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.TextField()
    fecha = models.DateField(auto_now_add = True)
    


    def __str__(self):
        return self.comment


