from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CreateCommentForm


from django.http import HttpResponse



@login_required
def save_comment(request):
    if request.method == 'POST':
        url = request.POST['url']
        post = {
            'user': request.user.pk,
            'comment': request.POST['comment'],
            'post': request.POST['post']
        }
        form = CreateCommentForm(post)
        if form.is_valid():
            form.save()
            return redirect('post:detalle')
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)

# Create your views here.
