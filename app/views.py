from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
# Create your views here.

def home(request):
    return render(request, 'home.html') 

def nosotros(request):
    return render(request, 'nosotros.html', {})

def libros(request):
    libros=Libro.objects.all()
    return render(request, 'libros/index.html', {'libros':libros})      

def crear_libro(request):
    return render(request, 'libros/crear.html')

def editar_libro(request):
    return render(request, 'libros/editar.html')