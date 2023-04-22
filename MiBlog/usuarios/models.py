from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.usuario)
    
    