from django.shortcuts import render
from django.http import HttpResponse, request

#Importaciones para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


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