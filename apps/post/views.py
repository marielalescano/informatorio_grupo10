from django.shortcuts import render,redirect
from .models import Post,Objetivo
from django.core.paginator import Paginator 
from apps.comentario.models import Comment
from apps.comentario.forms import CreateCommentForm

def listar_post(request): 
    
    #posts = Post.objects.all().order_by('user')
    #Post.objects.filter(estado = True).order_by('-fecha_creacion')
    posts = Post.objects.filter(estado = True)
    #Buscar funcion para obtener la peticion de form-1 Filtrar

    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)  

    return render(request,'post/listar_post.html', {'posts':posts})

    
def DetallePost(request, pk): # página para ver post

    posts = Post.objects.get(pk = pk)
    comments = Comment.objects.filter(post=pk)
    data = {
        'user':'user.username',
        'post':'posts.pk',
    }
    form = CreateCommentForm(data)

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            form.instance.post = Post.objects.get(pk=pk)
            form.instance.user = request.user
            form.save()
            return redirect ( 'post:listar_post')
    else:
        form = CreateCommentForm()
    
    ctx ={
        'posts':posts,
        'comments':comments,
        'form':form,
    }    

    return render(request, 'post/detalle_post.html',ctx )


def objetivos(request): # página donde se listan los objetivos como categorías
    
    objetivos = Objetivo.objects.filter(estado = True)
    paginator = Paginator(objetivos,3)
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




    