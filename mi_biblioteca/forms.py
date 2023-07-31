from django import forms

class LibroFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   genero = forms.CharField(required=True, max_length=64)
   sub_genero = forms.CharField(max_length=64)
   autor = forms.CharField(required=True, max_length=256)
   resumen = forms.CharField(required=True, max_length=256)
   anio = forms.IntegerField()

class GeneroFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=32)
   sub_genero = forms.CharField(max_length=128)

class AutorFormulario(forms.Form):
   apellido = forms.CharField(required=True, max_length=256)
   nombre = forms.CharField(required=True, max_length=256)
   fecha_nacimiento = forms.DateField()
   bio = forms.CharField(required=True, max_length=256)