from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Objetivo
from django.core.paginator import Paginator 
from apps.comentario.models import Comment
from apps.comentario.forms import CreateCommentForm

def listar_post(request): 

    opcion = request.GET.get('buscar')
    posts = Post.objects.all()
    if opcion == "1":
        posts = Post.objects.all().order_by('usuario')
    elif opcion == "2":
        posts=Post.objects.filter(estado = True).order_by('-fecha_creacion') 

    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)  

    return render(request,'post/listar_post.html', {'posts':posts})
    #posts = Post.objects.all().order_by('')
    #posts = Post.objects.all().order_by('user')
    #Post.objects.filter(estado = True).order_by('-fecha_creacion')
    
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
        #'comment':post.cantidad_comment(),
        'comment':comment,
        'likes': posts.cantidad_likes(),
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

def darlike(request, pk):

    post = get_object_or_404(Post, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('/post/detalle/'+str(post.id), {'Post': post, 'likes': post.cantidad_likes()} )

    """if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:"""