from django.urls import path
# from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.libros, name='libros'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('editar_libro/', views.editar_libro, name='editar_libro'),
]
