from django import forms 

#importacion para modelado de mis forms de usuarios
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, label='Apellido',widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        #mensajes de ayuda:
        help_texts = {k:"" for k in fields}
    
    def __init__(self, *args, **kwargs):
        super(UsuarioRegistroForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class PerfilEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, label='Apellido',widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, label='Usuario',widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    

    class Meta:
        model = User
        fields = ['username', 'password' , 'first_name', 'last_name', 'email', 'is_superuser']

        #mensajes de ayuda:
        help_texts = {k:"" for k in fields}
    