from django.shortcuts import render
from django.http import HttpResponse, request

#Importaciones para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

#Importaciones para views basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.models import post

# Create your views here.
def inicio(request):
    return render(request, 'core/home.html')
    
def login_form(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            datos = form.cleaned_data()

            usuario = datos['username']
            passw = datos['password']

            user = authenticate(username = usuario , password = passw)

            if user is not None:
                login(request, user)

                return render(request, "core/home.html", {"mensaje":f"Bienvendio {usuario}"})
            else:
                return render(request, "core/login.html", {"mensaje":"Usuario o contraseña incorrecta", "form": form})
        else:
            return render(request, "core/home.html", {"mensaje": "Error en el formulario"})

    else:
        form = AuthenticationForm()

    return render(request, "core/login.html", {"form":form})

class PostsListarView(ListView):
    model = post 
    template_name = 'core/posts_list.html'

class PostDetailView(DetailView):
    model = post
    template_name = 'core/post_detail.html'

class PostAddView(CreateView):
    model = post
    template_name = 'core/post_add.html'
    fields = '__all__'
