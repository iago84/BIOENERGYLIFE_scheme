from django.db import models

class Configuracion(models.Model):
    clave = models.CharField(max_length=100, unique=True)
    valor = models.CharField(max_length=255)

class Parametro(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=255)

class Log(models.Model):
    evento = models.CharField(max_length=100)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
