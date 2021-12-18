from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView 
from django.urls import reverse_lazy
from .forms import UserRegisterForm

def login(request):
    return render(request,'login.html')

class registro(CreateView):
   
    model = User
    template_name = "usuarios/registro.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    

def publicar(request):
    return render(request,'usuarios/publicar.html')

def profile(request):
    
    return render(request,'usuarios/profile.html')