from django.urls import path,include
from . import views

app_name = 'usuarios'

urlpatterns=[

    path('login/',views.login, name = 'login'),
    path('registro/',views.registro, name = 'registro'),

]
