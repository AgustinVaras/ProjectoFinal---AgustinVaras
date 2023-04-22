from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextField(blank=True, null=True)
    foto_perfil = models.ImageField(null=True, blank=True, upload_to="Perfil/")
    
    website_url = models.URLField(max_length=150 ,null=True, blank=True)
    ig_url = models.URLField(max_length=150, null=True, blank=True)
    facebook_url = models.URLField(max_length=150 ,null=True, blank=True)

    def __str__(self):
        return str(self.usuario)
    
    