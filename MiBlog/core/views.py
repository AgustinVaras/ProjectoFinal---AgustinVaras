from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request

#Importaciones para views basadas en clases
#----------------------------------------------------------------------------------------------------------------------------------------------
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Importaciones para validaciones de usuarios
#----------------------------------------------------------------------------------------------------------------------------------------------
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

def CategoriasView(request, cats=None):
    categoria = None
    posts = None
    if cats:
        try:
            categoria = Categoria.objects.get(nombre=str(cats).replace('-',' '))
        except Exception as e:
            categoria = 'Inexistente'
        else:
            posts = Post.objects.filter(categoria=categoria)

        # posts = get_object_or_404(Post, categoria=categoria)
    return render(request, 'core/categoria_list.html', {'categoria':str(categoria).capitalize(), 'posts':posts})
    

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
