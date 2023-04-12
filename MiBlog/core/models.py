from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#Crear modelos para blogs, usuarios


class post(models.Model):
    #Propiedades propias del post
    titulo = models.CharField(max_length=50, help_text="Titulo del post")
    subtitulo = models.CharField(max_length=100, help_text="Subtitulo")
    cuerpo = models.TextField()

    #Foreign key a usuarios
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Propiedades de fecha
    creacion = models.DateField(auto_now_add=True)
    ultima_mod = models.DateField(auto_now=True)

    img = models.ImageField(blank=True,upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return f"{self.titulo} | {self.subtitulo}"

    def get_absolute_url(self):
        return reverse('Detail_Post', args=(str(self.id)) )
    