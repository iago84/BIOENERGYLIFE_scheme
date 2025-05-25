from django.db import models

class Organulo(models.Model):
    nombre = models.CharField(max_length=100, default="")
    tipo = models.CharField(max_length=50, default="")
    es_secuenciador = models.BooleanField(default=False)
    potencia = models.FloatField(default=0.0)
    estado = models.CharField(max_length=50, default="operativo")
    parametros_operacion = models.JSONField(blank=True, null=True)
    celula_asociada = models.CharField(max_length=100, blank=True, null=True)  # O un FK si lo tienes
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre or f"Organulo {self.pk}"

class TipoOrganulo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    parametros_defecto = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Secuenciador(models.Model):
    organulo = models.ForeignKey(Organulo, on_delete=models.CASCADE, related_name='secuenciadores')
    estado = models.CharField(max_length=20, choices=[
        ("listo", "Listo"),
        ("operando", "Operando"),
        ("error", "Error")
    ], default="listo")
    ultima_activacion = models.DateTimeField(blank=True, null=True)
    parametros = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Secuenciador de {self.organulo}"

class DispositivoControl(models.Model):
    nombre = models.CharField(max_length=100, default="")
    tipo = models.CharField(max_length=50, default="control")
    organulo = models.ForeignKey(Organulo, on_delete=models.CASCADE, related_name='dispositivos_control', blank=True, null=True)
    parametros = models.JSONField(blank=True, null=True)
    estado = models.CharField(max_length=50, default="operativo")

    def __str__(self):
        return self.nombre or f"DispositivoControl {self.pk}"
