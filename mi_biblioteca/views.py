from django.shortcuts import render, redirect
from django.urls import reverse

from mi_biblioteca.models import Libro, Generos, Autores
from mi_biblioteca.forms import LibroFormulario, GeneroFormulario, AutorFormulario

def listar_libros(request):
    contexto = {
        "libros": Libro.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_biblioteca/lista_libros.html',
        context=contexto,
    )
    return http_response

def listar_generos(request):
    contexto = {
        "generos": Generos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_biblioteca/lista_generos.html',
        context=contexto,
    )
    return http_response

def listar_autores(request):
    contexto = {
        "autores": Autores.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_biblioteca/lista_autores.html',
        context=contexto,
    )
    return http_response

def crear_libros(request):
   if request.method == "POST":
       formulario = LibroFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre"]
           genero = data["genero"]
           sub_genero = data["sub_genero"]
           autor = data["autor"]
           resumen = data["resumen"]
           anio = data["año"]
           curso = Libro(nombre=nombre, genero=genero, sub_genero=sub_genero, autor=autor, resumen=resumen, anio=anio)
           curso.save()

           url_exitosa = reverse('lista_libros')
           return redirect(url_exitosa)
   else: 
       formulario = LibroFormulario()
   http_response = render(
       request=request,
       template_name='mi_biblioteca/formulario_libros.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_generos(request):
   if request.method == "POST":
       formulario = GeneroFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre"]
           sub_genero = data["sub_genero"]
           curso = Generos(nombre=nombre,sub_genero=sub_genero)
           curso.save()

           url_exitosa = reverse('lista_generos')
           return redirect(url_exitosa)
   else: 
       formulario = GeneroFormulario()
   http_response = render(
       request=request,
       template_name='mi_biblioteca/formulario_generos.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_autores(request):
   if request.method == "POST":
       formulario = AutorFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre"]
           apellido = data["apellido"]
           fecha_nacimiento = data["fecha_nacimiento"]      
           bio = data["bio"]     
           curso = Autores(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, bio=bio)
           curso.save()

           url_exitosa = reverse('lista_autores')
           return redirect(url_exitosa)
   else: 
       formulario = AutorFormulario()
   http_response = render(
       request=request,
       template_name='mi_biblioteca/formulario_autores.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_libros(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       libros = Libro.objects.filter(nombre__contains=busqueda)
       contexto = {
           "libros": libros,
       }
       http_response = render(
           request=request,
           template_name='mi_biblioteca/lista_libros.html',
           context=contexto,
       )
       return http_response


