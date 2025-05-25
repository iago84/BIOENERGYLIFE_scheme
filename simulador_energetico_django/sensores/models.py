from django.db import models

class TipoSensor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50, default="eléctrico")  # Ej: eléctrico, térmico, mecánico, ambiental

    def __str__(self):
        return self.nombre

class Sensor(models.Model):
    nombre = models.CharField(max_length=100, default="")
    tipo = models.CharField(max_length=50, default="desconocido")
    tipo_sensor = models.ForeignKey(TipoSensor, on_delete=models.SET_NULL, null=True, blank=True)

    umbral_alerta = models.FloatField(default=0.0, help_text="Valor de umbral para disparar alerta")
    intervalo_medicion = models.IntegerField(default=60, help_text="Intervalo en segundos entre mediciones")
    estado = models.CharField(max_length=20, default="ok", choices=[("ok", "OK"), ("alerta", "Alerta"), ("error", "Error")])
    ultima_medicion = models.FloatField(default=0.0)
    unidad = models.CharField(max_length=20, default="kW")
    metadatos = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Medidor(models.Model):
    tipo = models.CharField(max_length=50, default="multímetro")
    precision = models.FloatField(default=0.01)
    intervalo_lectura = models.IntegerField(default=60)
    valor_actual = models.FloatField(default=0.0)
    unidad = models.CharField(max_length=20, default="kW")

    asociado_a_sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=20, default="activo", choices=[("activo", "Activo"), ("apagado", "Apagado"), ("error", "Error")])
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} ({self.valor_actual} {self.unidad})"
