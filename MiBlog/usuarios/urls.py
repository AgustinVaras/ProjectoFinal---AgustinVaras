from django.urls import path
from .views import UsuarioRegistroView, UsuarioEditView, PasswordsChangeView, PerfilDetailView
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('registro/', UsuarioRegistroView.as_view(), name='Registro'),
    path('editar/', UsuarioEditView.as_view(), name='Editar_Usuario'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/perfil', PerfilDetailView.as_view(), name='Perfil_Detail'),
]
