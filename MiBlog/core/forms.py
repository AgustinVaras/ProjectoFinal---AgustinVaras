from django import forms 
from phonenumber_field.formfields import PhoneNumberField
from .models import post


class PostAddForm(forms.ModelForm):
    class Meta:
        model = post 
        fields = ('titulo', 'subtitulo', 'cuerpo', 'author')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del post'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitulo del post'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            #'img': forms.ImageField(attrs={'class': 'form-control'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('titulo', 'subtitulo', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del post'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitulo del post'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }
