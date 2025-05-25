from django.db import models

class Celula(models.Model):
    nombre = models.CharField(max_length=100, default="")
    tipo = models.CharField(max_length=50, default="")
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    fecha_activacion = models.DateTimeField(auto_now_add=True)
    estado_funcional = models.CharField(
        max_length=50,
        choices=[("activa", "Activa"), ("latente", "Latente"), ("inactiva", "Inactiva")],
        default="activa"
    )
    energia_actual = models.FloatField(default=0.0)
    energia_maxima = models.FloatField(default=0.0)
    nivel_evolucion = models.IntegerField(default=1)
    historial = models.JSONField(blank=True, null=True)
    puede_multiplicar = models.BooleanField(default=False)
    enlaces = models.JSONField(blank=True, null=True, help_text="IDs de conexiones funcionales")
    posibles_evoluciones = models.JSONField(blank=True, null=True)
    productiva = models.BooleanField(default=True)
    consumo_kw = models.FloatField(default=0.0)
    produccion_kw = models.FloatField(default=0.0)
    generadores = models.JSONField(blank=True, null=True)
    organulos = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.nombre or f"Celula {self.pk}"

class EstadoCelula(models.Model):
    celula = models.ForeignKey(Celula, on_delete=models.CASCADE, related_name='estados')
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Estado de {self.celula} en {self.fecha:%Y-%m-%d %H:%M}"

class EvolucionCelula(models.Model):
    celula = models.ForeignKey(Celula, on_delete=models.CASCADE, related_name='evoluciones')
    fecha = models.DateTimeField(auto_now_add=True)
    tipo_evolucion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    nueva_celula = models.ForeignKey(Celula, on_delete=models.SET_NULL, null=True, blank=True, related_name='origen_evolucion')

    def __str__(self):
        return f"{self.celula} evolucionó a {self.nueva_celula} ({self.tipo_evolucion})"

class UbicacionCelula(models.Model):
    celula = models.OneToOneField(Celula, on_delete=models.CASCADE, related_name='ubicacion_detallada')
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)
    z = models.FloatField(default=0.0)

    def __str__(self):
        return f"Ubicación de {self.celula}: ({self.x}, {self.y}, {self.z})"
