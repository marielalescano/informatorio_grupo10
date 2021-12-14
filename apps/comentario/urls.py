from django.urls import path,include
from . import views 

app_name = 'comentario'

urlpatterns=[
        path(
                route='posts/save_comment',
                view=views.save_comment,
                name='save_comment'
    ),

]
