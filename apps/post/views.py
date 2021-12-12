from django.shortcuts import render
from .models import Post,Objetivo
from django.core.paginator import Paginator 

def listar_post(request): #página de lista de post

    posts = Post.objects.filter(estado = True)  
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request,'post/listar_post.html', {'posts':posts})

    
def DetallePost(request, pk): # página para ver post

    posts = Post.objects.get(pk = pk)

    return render(request, 'post/detalle_post.html',{'posts':posts})



def objetivos(request): # página donde se listan los objetivos como categorías
    
    objetivos = Objetivo.objects.filter(estado = True)

    return render(request,'post/objetivos.html',{'objetivos': objetivos})




def listarPostObjetivos(request,pk): # página donde se listan los post segun el objetivo selecc.

    objetivo = Objetivo.objects.get(pk = pk)
    posts = Post.objects.filter( objetivo = objetivo)
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'post/objetivos_post.html', {'posts': posts})