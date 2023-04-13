from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#Crear modelos para blogs, usuarios


class post(models.Model):
    #Propiedades propias del post
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()

    #Foreign key a usuarios
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Propiedades de fecha
    creacion = models.DateField(auto_now_add=True)
    ultima_mod = models.DateField(auto_now=True)

    #img = models.ImageField(blank=True,upload_to='.\posts-img/')

    def __str__(self) -> str:
        return f"{self.titulo} | {self.subtitulo}"

    def get_absolute_url(self):
        return reverse('Detail_Post', args=(str(self.id)) )
    