from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

#Crear modelos para blogs, usuarios


class Categoria(models.Model):
    nombre = models.CharField(max_length=75, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('home')
    
    def save(self,  *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super(Categoria, self).save(*args, **kwargs)
    


class Post(models.Model):
    #Propiedades propias del post
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    snippet = models.CharField(max_length=250, default="Resumen del post. . .")
    cuerpo = RichTextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='SinCategoria')
    header_imagen = models.ImageField(null=True, blank=True, upload_to="posts-img/")

    #Foreign key a usuarios
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Propiedades de fecha
    creacion = models.DateField(auto_now_add=True)
    ultima_mod = models.DateField(auto_now=True)

    #img = models.ImageField(blank=True,upload_to='.\posts-img/')

    def __str__(self) -> str:
        return f"{self.titulo} | {self.subtitulo}"

    def get_absolute_url(self):
        return reverse('Detail_Post', kwargs={'pk':self.pk})


    