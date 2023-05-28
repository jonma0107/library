from django.urls import path
# from .views import *
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.libros, name='libros'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('editar_libro/<int:id>', views.editar_libro, name='editar_libro'),
    path('eliminar_libro/<int:id>', views.eliminar_libro, name='eliminar_libro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
