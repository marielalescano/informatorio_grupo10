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
from django.contrib import messages

def login(request):
    return render(request,'login.html')

@login_required
def profile(request):

    user_post = Post.objects.filter(user = request.user)
    profile = Profile.objects.get( user = request.user)
    ctx ={
        'posts':user_post,
        'profile': profile,
    }

    return render(request,'usuarios/profile.html',ctx)


class CrearPerfil(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'usuarios/crearperfil.html'
    form_class = CrearPerfil 

    def get_success_url(self):
        messages.success(
            self.request, 'Perfil creado satisfactoriamente')
        return reverse_lazy("usuarios:profile")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)




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
        messages.success(
            self.request, 'Tu perfil se ha actualizado correctamente.')
        return reverse_lazy("usuarios:profile")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class registro(CreateView):
   
    model = User
    template_name = "usuarios/registro.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')





     