from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request

#Importaciones para views basadas en clases
#----------------------------------------------------------------------------------------------------------------------------------------------
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Importaciones para mis modelos y forms
#----------------------------------------------------------------------------------------------------------------------------------------------
from core.models import Post, Categoria
from .forms import PostAddForm, PostEditForm

# Create your views here.
def inicio(request):
    return render(request, 'core/home.html')


#List Views
class PostsListarView(ListView):
    model = Post 
    template_name = 'core/posts_list.html'
    ordering = ['-ultima_mod']

def CategoriasView(request, cats):
    categ = Categoria.objects.get(nombre=cats)
    posts_categoria = Post.objects.filter(categoria=categ)
    return render(request, 'core/categoria_list.html', {'posts':posts_categoria,'cats':cats, 'categ':categ})

#Detail Vies
class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'

#Add Views
class PostAddView(CreateView):
    model = Post
    form_class =  PostAddForm
    template_name = 'core/post_add.html'

class CategAddView(CreateView):
    model = Categoria 
    template_name = 'core/categoria_add.html'
    fields = '__all__'

#Edit Views
class PostEditView(UpdateView):
    model = Post
    form_class =  PostEditForm
    template_name = 'core/post_edit.html'

#Delete Views
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'core/post_delete.html'
    success_url = reverse_lazy('List_Posts')
