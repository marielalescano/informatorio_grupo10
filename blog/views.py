from django.shortcuts import render
from apps.post.models import Post
from apps.comentario.models import Comment
from django.db.models import Count


def home(request):

    posts= Post.objects.all().order_by('likes')
    post = posts[:3]
    ultimos_post= Post.objects.all().order_by('-fecha_creacion')
    ultimos_post = ultimos_post[:3]
    ctx={
        'post':post,
        'ultimos_post':ultimos_post,
    }

    return render(request,'index.html',ctx)