from django import forms
from webalumnos.models import Curso, Profesor, Alumno


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'duracion_horas']


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellidos', 'email', 'cursos_asignados']


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellidos', 'email', 'curso']


#Consultar base de datos

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)
