from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView 
from django.urls import reverse_lazy



def login(request):
    return render(request,'login.html')

class registro(CreateView):
   
    model = Profile
    template_name = "usuarios/registro.html"
    form_class = UserCreationForm 
    success_url = reverse_lazy('home')

    

def publicar(request):
    return render(request,'usuarios/publicar.html')
