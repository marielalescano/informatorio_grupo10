from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserRegisterForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name',]
        help_texts = {k:"" for k in fields }

class CrearPerfil(forms.ModelForm):

    class Meta:
        model = Profile 
        fields =['website', 'photo']



class PasswordChangedForm (PasswordChangeForm):  

    class Meta:
        model = User 
        fields =['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields }        