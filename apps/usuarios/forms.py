from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name',]
        help_texts = {k:"" for k in fields }