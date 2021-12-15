
from django import forms


# Models


from .models import Comment
from django.contrib.auth.models import User

class CreateCommentForm(forms.ModelForm):
   
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        
        model = Comment
        fields = ('user', 'post', 'comment')



