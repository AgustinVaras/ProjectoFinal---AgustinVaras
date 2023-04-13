from django.shortcuts import render
from django.http import HttpResponse, request

#Importaciones para el login
#----------------------------------------------------------------------------------------------------------------------------------------------
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

#Importaciones para views basadas en clases
#----------------------------------------------------------------------------------------------------------------------------------------------
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Importaciones para mis modelos y forms
#----------------------------------------------------------------------------------------------------------------------------------------------
from core.models import post
from .forms import PostAddForm, PostEditForm

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
    form_class =  PostAddForm
    template_name = 'core/post_add.html'

class PostEditView(UpdateView):
    model = post
    form_class =  PostEditForm
    template_name = 'core/post_edit.html'

class PostDeleteView(DeleteView):
    model = post
    template_name = 'core/post_delete.html'
    success_url = reverse_lazy('List_Posts')