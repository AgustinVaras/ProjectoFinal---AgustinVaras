from django import forms 
from phonenumber_field.formfields import PhoneNumberField
from .models import Post, Categoria

# categorias = categoria.objects.all().values_list('nombre','nombre')

# list_categorias = []

# for item in categorias:
#     list_categorias.append(item)

class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('titulo', 'subtitulo','categoria', 'cuerpo', 'snippet', 'author')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del post'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitulo del post'}),
            'categoria':forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve resumen del post'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'elder', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control','value':'', 'id':'elder'}),
            #'img': forms.ImageField(attrs={'class': 'form-control'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'categoria', 'cuerpo', 'snippet')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del post'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitulo del post'}),
            'categoria':forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve resumen del post'}),
        }
