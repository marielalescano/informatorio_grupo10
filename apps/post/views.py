from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Objetivo
from django.core.paginator import Paginator 
from apps.comentario.models import Comment
from apps.comentario.forms import CreateCommentForm
from .forms import AltaPost
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy



class AltaPost(CreateView):
    model = 'Post'
    template_name = 'post/publicar.html'
    form_class = AltaPost
    success_url = reverse_lazy('home')



def listar_post(request): 

    opcion = request.GET.get('select')
    posts = Post.objects.all()
    if opcion == "1":
        posts = Post.objects.all().order_by('usuario')
    elif opcion == "2":
        posts=Post.objects.all().order_by('fecha_creacion') 
    #elif opcion == "3":



    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)  

    return render(request,'post/listar_post.html', {'posts':posts})

    
def DetallePost(request, pk): # página para ver post

    posts = Post.objects.get(pk = pk)
    comments = Comment.objects.filter(post=pk)
    comment = comments.count()

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
            return redirect ( '/post/detalle/'+str(posts.id))
    else:
        form = CreateCommentForm()
    
    ctx ={
        'posts':posts,
        'comments':comments,
        'form':form,
        'comment':comment,
        'likes': posts.cantidad_likes(),
    }    

    return render(request, 'post/detalle_post.html',ctx )
  



def objetivos(request):
    
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

def darlike(request, pk):

    post = get_object_or_404(Post, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('/post/detalle/'+str(post.id), {'Post': post, 'likes': post.cantidad_likes()} )

