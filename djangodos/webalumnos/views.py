from django.shortcuts import render
from django.shortcuts import render, redirect
from webalumnos.forms import CursoForm, ProfesorForm, AlumnoForm

from webalumnos.forms import BusquedaForm
from webalumnos.models import Curso, Profesor, Alumno

# Create your views here.



def base(request):
    return render(request, 'base.html')


def formulario_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = CursoForm()
    return render(request, 'formulario_curso.html', {'form': form})


def formulario_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = ProfesorForm()
    return render(request, 'formulario_profesor.html', {'form': form})


def formulario_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = AlumnoForm()
    return render(request, 'formulario_alumno.html', {'form': form})






def buscar(request):
    form = BusquedaForm(request.GET)
    resultados_cursos = None
    resultados_profesores = None
    resultados_alumnos = None
    
    if form.is_valid():
        busqueda = form.cleaned_data['busqueda']
        resultados_cursos = Curso.objects.filter(nombre__icontains=busqueda)
        resultados_profesores = Profesor.objects.filter(nombre__icontains=busqueda) | \
                                Profesor.objects.filter(apellidos__icontains=busqueda)
        resultados_alumnos = Alumno.objects.filter(nombre__icontains=busqueda) | \
                              Alumno.objects.filter(apellidos__icontains=busqueda)
    
    return render(request, 'buscar.html', {'form': form,
                                           'resultados_cursos': resultados_cursos,
                                           'resultados_profesores': resultados_profesores,
                                           'resultados_alumnos': resultados_alumnos})

