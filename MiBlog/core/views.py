from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def inicio(request):
    return render(request, 'core/index.html')
    
