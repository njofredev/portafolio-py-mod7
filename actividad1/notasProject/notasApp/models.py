from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    puntaje = models.FloatField()