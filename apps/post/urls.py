from django.urls import path,include
from . import views

app_name = 'post'

urlpatterns=[

    path('listar/',views.listar_post, name = 'listar_post')
    

]





