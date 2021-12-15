"""User forms."""

# Django
from django import forms

# Models
from .models import Comment
from django.contrib.auth.models import User

class CreateCommentForm(forms.ModelForm):
    """Post model form."""

    comment = forms.CharField(widget=forms.Textarea)


    class Meta:
        """Form settings."""

        model = Comment
        fields = ('user', 'post', 'comment')