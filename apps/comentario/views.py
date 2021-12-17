from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CreateCommentForm




@login_required
def enviado(request):

    return render(request, 'comentario/enviado.html')



