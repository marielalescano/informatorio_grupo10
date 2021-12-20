from django.shortcuts import render, redirect
from apps.post.models import Post
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, CrearPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#Utilizamos el login por defecto de django: username y contraseña.

def login(request):

    return render(request,'login.html')


# Función para mostrar al usuario sus publicaciones (Acceso a crear editar y eliminar)

@login_required
def profile(request):

    user_post = Post.objects.filter(user = request.user)
    
    ctx ={
        'posts':user_post,
    }

    return render(request,'usuarios/profile.html', ctx )


#Clase para el registro de usuarios.

class registro(CreateView):
   
    model = User
    template_name = "usuarios/registro.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def get_success_url(self):

        return reverse_lazy("usuarios:profile")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)    

#Clase para crear perfil de usuario, agregar imágen de perfil y website

class CrearPerfil(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'usuarios/crearperfil.html'
    form_class = CrearPerfil 

    def get_success_url(self):

        return reverse_lazy("usuarios:profile")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)



# Clase para editar Perfil (cambiar foto de perfil y website)

class ActualizarPerfil(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'usuarios/actualizarperfil.html'
    fields=['website','photo',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):

        return reverse_lazy("usuarios:profile")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)








     