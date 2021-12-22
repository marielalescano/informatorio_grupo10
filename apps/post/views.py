from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Objetivo
from django.core.paginator import Paginator 
from apps.comentario.models import Comment
from apps.comentario.forms import CreateCommentForm
from .forms import AltaPost
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Con esta clase el usuario puede dar de alta un post.

class AltaPost(LoginRequiredMixin, CreateView):
    
    model = Post
    template_name = 'post/publicar.html'
    form_class = AltaPost 

    def get_success_url(self):
        messages.success(
            self.request, 'Tu publicación ha sido creada con éxito')
        return reverse_lazy("home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

#Con esta clase el usuario puede modificar sus post.

class ActualizarPost(LoginRequiredMixin, UpdateView):

    model = Post
    template_name = 'post/actualizar.html'
    fields = ["titulo", "descripcion", "contenido", "imagen",'objetivo',] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        return reverse_lazy("usuarios:profile")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)



#Con esta clase el usuario puede eliminar un post.

class EliminarPost(LoginRequiredMixin, DeleteView):

    model = Post

    def get_success_url(self):
        return reverse_lazy("usuarios:profile")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


#Con esta función se listan las publicaciones, primero se listan de forma predeterminada
#Luego se se recibe una consulta desde la página a la que hace referencia la vista
#se filtra y se orfena según lo requerido.

def listar_post(request): 

    opcion = request.GET.get('select')
    posts = Post.objects.all().order_by('-fecha_creacion')

    if opcion == "1":
        posts = Post.objects.all().order_by('objetivo')
    elif opcion == "2":
        posts=Post.objects.all().order_by('fecha_creacion') 
    elif opcion == "3":
        posts = Post.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')

    return render(request,'post/listar_post.html', {'posts':posts})


"""Con esta función se muestra el post en particular, se listan los comentarios
del post, y se habilita un formulario para comentar""" 

def DetallePost(request, pk): 

    posts = Post.objects.get(pk = pk)
    lista_comentarios = Comment.objects.filter(post=pk)
    comentario = lista_comentarios.count()
    
    data = {
        'user':'user.username', # Aquí se toma el usuario conectado
        'post':'posts.pk', # Aquí se toma el post al que está comentando
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
        'comentarios':lista_comentarios,
        'form':form,
        'comentario':comentario,
        'likes': posts.cantidad_likes(),
    }    

    return render(request, 'post/detalle_post.html',ctx )
  


"""Con esta función se listan los objetivos como categorías"""
def objetivos(request):
    
    objetivos = Objetivo.objects.all()
    paginator = Paginator(objetivos,4)
    page = request.GET.get('page')
    objetivos = paginator.get_page(page)

    return render(request,'post/objetivos.html',{'objetivos': objetivos})

# Con esta función se listan los post según el objetivo

def listarPostObjetivos(request,pk): 

    objetivo = Objetivo.objects.get(pk = pk)
    posts = Post.objects.filter( objetivo = objetivo)
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'post/objetivos_post.html', {'posts': posts})

# Con esta función se establece que un usuario puede dar like a un post, solo una vez
# si da 2 click la seguna vez elimina el like y necesita estar logueado para hacerlo.

@login_required
def darlike(request, pk):

    post = get_object_or_404(Post, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('/post/detalle/'+str(post.id), {'Post': post, 'likes': post.cantidad_likes()} )

