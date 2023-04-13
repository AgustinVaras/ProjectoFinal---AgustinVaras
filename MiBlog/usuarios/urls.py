from django.urls import path
from .views import UsuarioRegistroView

urlpatterns = [
    path('usuarios/', UsuarioRegistroView.as_view(), name='Registro'),
    
]
