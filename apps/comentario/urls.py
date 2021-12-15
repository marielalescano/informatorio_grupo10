from django.urls import path,include
from . import views 

app_name = 'comentario'

urlpatterns=[
        path('posts/save_comment',views.save_comment,name='save_comment'),

]
