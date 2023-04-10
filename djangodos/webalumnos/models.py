from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_horas = models.IntegerField()
    
    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    cursos_asignados = models.ManyToManyField(Curso)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

