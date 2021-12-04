from django.shortcuts import render


def listar_post(request):
    return render(request,'post/listar_post.html')



