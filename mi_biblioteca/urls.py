from django.urls import path

from mi_biblioteca.views import (listar_libros, listar_generos, listar_autores, crear_libros, crear_generos, crear_autores, buscar_libros)

urlpatterns = [
    path("libros/", listar_libros, name='lista_libros'),
    path("generos/", listar_generos, name='lista_generos'),
    path("autores/", listar_autores, name='lista_autores'),
    path("crear_libro/", crear_libros, name='crear_libros'),
    path("crear_genero/", crear_generos, name='crear_generos'),
    path("crear_autor/", crear_autores, name='crear_autores'),
    path("buscar_libro/", buscar_libros, name='buscar_libros'),
]