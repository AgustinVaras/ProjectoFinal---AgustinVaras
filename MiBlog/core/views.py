from django.shortcuts import render
from django.http import HttpResponse, request

#Importaciones para views basadas en clases
#----------------------------------------------------------------------------------------------------------------------------------------------
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Importaciones para mis modelos y forms
#----------------------------------------------------------------------------------------------------------------------------------------------
from core.models import post, categoria
from .forms import PostAddForm, PostEditForm

# Create your views here.
def inicio(request):
    return render(request, 'core/home.html')


#List Views
class PostsListarView(ListView):
    model = post 
    template_name = 'core/posts_list.html'
    ordering = ['-ultima_mod']

def CategoriasView(request, cats):
    posts_categoria = post.objects.filter(categoria=cats)
    return render(request, 'categorias_list.html', {'posts': posts_categoria})

#Detail Vies
class PostDetailView(DetailView):
    model = post
    template_name = 'core/post_detail.html'

#Add Views
class PostAddView(CreateView):
    model = post
    form_class =  PostAddForm
    template_name = 'core/post_add.html'

class CategAddView(CreateView):
    model = categoria 
    template_name = 'core/categoria_add.html'
    fields = '__all__'

#Edit Views
class PostEditView(UpdateView):
    model = post
    form_class =  PostEditForm
    template_name = 'core/post_edit.html'

#Delete Views
class PostDeleteView(DeleteView):
    model = post
    template_name = 'core/post_delete.html'
    success_url = reverse_lazy('List_Posts')
