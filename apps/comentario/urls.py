from django.urls import path,include
from . import views 

app_name = 'comentario'

urlpatterns=[
        path('enviado',views.enviado,name='enviado'),

]
