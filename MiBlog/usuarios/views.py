from django.shortcuts import render, get_object_or_404

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
from .models import Perfil

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

class PerfilDetailView(generic.DetailView):
    model = Perfil
    template_name = 'registration/perfil_usuario.html'

    def get_context_data(self, *args, **kwargs):
        usuario = Perfil.objects.all()
        context = super(PerfilDetailView, self).get_context_data(*args, **kwargs)

        perfil_usuario = get_object_or_404(Perfil, id=self.kwargs['pk'])

        context["perfil_usuario"] = perfil_usuario
        return context
