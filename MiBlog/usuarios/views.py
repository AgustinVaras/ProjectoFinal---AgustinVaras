from django.shortcuts import render

#Importaciones para el login
#----------------------------------------------------------------------------------------------------------------------------------------------
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

#Importaciones de mis modelos y forms
#----------------------------------------------------------------------------------------------------------------------------------------------
from .forms import UsuarioRegistroForm, PerfilEditForm, PasswordChangingForm

# Create your views here
class UsuarioRegistroView(generic.CreateView):
    form_class = UsuarioRegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')


class UsuarioEditView(generic.UpdateView):
    form_class = PerfilEditForm
    template_name = 'registration/perfil_editar.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
