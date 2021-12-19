from django.urls import path,include
from . import views 
from .views import *


app_name = 'post'

urlpatterns=[

    path('listar/',views.listar_post, name = 'listar_post'),
    path('detalle/<int:pk>', views.DetallePost, name= 'detalle'),
    path('objetivos/',views.objetivos,name='objetivos'),
    path('listarPostObjetivos/<int:pk>', views.listarPostObjetivos, name= 'listarPostObjetivos'),
    path('like/<int:pk>', views.darlike, name='darlike'),
    path('publicar/', AltaPost.as_view(), name='publicar'),
    path('actualizar/<int:pk>/', ActualizarPost.as_view(), name='actualizar_post'),
    path('eliminar/<int:pk>/', EliminarPost.as_view(), name='eliminar_post'),
]





