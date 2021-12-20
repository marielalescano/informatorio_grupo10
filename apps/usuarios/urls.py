from django.urls import path,include
from . import views
from .views import *

app_name = 'usuarios'

urlpatterns=[

    path('login/',views.login, name = 'login'),
    path('registro/',views.registro.as_view(), name = 'registro'),
    path('profile/',views.profile, name = 'profile'),
    path('actualizar/<int:pk>/', ActualizarPerfil.as_view(), name='actualizarPerfil'),
    path('password-change/',PasswordChange.as_view(), name = 'passwordchange'),   
    path('password_success',views.password_success, name= 'password_success'),
]
