from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CreateCommentForm


@login_required
def save_comment(request):
    if request.method == 'POST':
        url = request.POST['url']
        post = {
            'user': request.user.id,
            'comment': request.POST['comment'],
            'post': request.POST['post']
        }
        form = CreateCommentForm(post)
        if form.is_valid():
            form.save()
            return redirect('post:detalle', url=url)
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)

# Create your views here.
