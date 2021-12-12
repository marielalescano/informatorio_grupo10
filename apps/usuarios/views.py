from django.shortcuts import render


def login(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'usuarios/registro.html')


def publicar(request):
    return render(request,'usuarios/publicar.html')
