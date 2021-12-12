from django.urls import path,include
from . import views 

app_name = 'post'

urlpatterns=[

    path('listar/',views.listar_post, name = 'listar_post'),
    path('detalle/<int:pk>', views.DetallePost, name= 'detalle'),
    path('objetivos/',views.objetivos,name='objetivos'),
    path('listarPostObjetivos/<int:pk>', views.listarPostObjetivos, name= 'listarPostObjetivos'),

]





