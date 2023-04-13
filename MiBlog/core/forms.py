from django import forms 
from phonenumber_field.formfields import PhoneNumberField
from .models import post

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        #mensajes de ayuda:
        help_texts = {k:"" for k in fields}

class PostAddForm(forms.ModelForm):
    class Meta:
        model = post 
        fields = ('titulo', 'subtitulo', 'cuerpo', 'author')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del post'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitulo del post'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            #'img': forms.ImageField(attrs={'class': 'form-control'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('titulo', 'subtitulo', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del post'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitulo del post'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }
