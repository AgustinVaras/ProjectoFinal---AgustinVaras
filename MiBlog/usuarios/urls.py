from django.urls import path
from .views import UsuarioRegistroView, UsuarioEditView

urlpatterns = [
    path('usuarios/', UsuarioRegistroView.as_view(), name='Registro'),
    path('usuarios/editar/', UsuarioEditView.as_view(), name='Editar_Usuario'),
]
