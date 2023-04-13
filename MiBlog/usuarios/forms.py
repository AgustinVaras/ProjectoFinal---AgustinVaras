from django import forms 

#importacion para modelado de mis forms de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsuarioRegistroForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        #mensajes de ayuda:
        help_texts = {k:"" for k in fields}