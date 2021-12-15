from django.shortcuts import render
from .models import Post,Objetivo
from django.core.paginator import Paginator 
from apps.comentario.models import Comment


def listar_post(request): #página de lista de post

    posts = Post.objects.filter(estado = True)

    form= CreateCommentForm()
    comments= CreateCommentForm.objects.filter(request.POST).order_by('-create_on')
    if form.is_valid():
        new_comments=form.save(commit=False)
        new_comments=request.user
        new_comments.post=post
        new_comments.save()


    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request,'post/listar_post.html', {'posts':posts})

    
def DetallePost(request, pk): # página para ver post

    posts = Post.objects.get(pk = pk)
    form= CreateCommentForm()
    comments= CreateCommentForm.objects.filter(posts=posts).order_by('-create_on')


    return render(request, 'post/detalle_post.html',{'posts':posts},{'comments':comments})

    return render(request, 'post/detalle_post.html',{'posts':posts} )




def objetivos(request): # página donde se listan los objetivos como categorías
    
    objetivos = Objetivo.objects.filter(estado = True)
    paginator = Paginator(objetivos,10)
    page = request.GET.get('page')
    objetivos = paginator.get_page(page)
    return render(request,'post/objetivos.html',{'objetivos': objetivos})


def listarPostObjetivos(request,pk): # página donde se listan los post segun el objetivo selecc.

    objetivo = Objetivo.objects.get(pk = pk)
    posts = Post.objects.filter( objetivo = objetivo)
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'post/objetivos_post.html', {'posts': posts})