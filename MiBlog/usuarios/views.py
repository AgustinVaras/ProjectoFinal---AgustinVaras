from django.shortcuts import render

#Importaciones para el login
#----------------------------------------------------------------------------------------------------------------------------------------------
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

#Importaciones de mis modelos y forms
#----------------------------------------------------------------------------------------------------------------------------------------------
from .forms import UsuarioRegistroForm

# Create your views here
class UsuarioRegistroView(generic.CreateView):
    form_class = UsuarioRegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

