from django import forms
from .models import Post


class AltaPost(forms.ModelForm):
   
    class Meta:
        model = Post
        fields = ('titulo','descripcion','contenido','imagen','objetivo',)