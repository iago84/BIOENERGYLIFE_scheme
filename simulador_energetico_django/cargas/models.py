from django.db import models

class TipoCarga(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    naturaleza = models.CharField(
        max_length=50,
        default="resistiva",
        choices=[
            ("resistiva", "Resistiva"),
            ("inductiva", "Inductiva"),
            ("capacitiva", "Capacitiva"),
            ("mixta", "Mixta")
        ]
    )

    def __str__(self):
        return self.nombre

class Carga(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, default="resistiva")
    tipo_carga = models.ForeignKey(TipoCarga, on_delete=models.SET_NULL, null=True, blank=True)

    potencia_nominal_kw = models.FloatField(default=0.0, help_text="Consumo nominal en kilovatios")
    consumo_instantaneo_kw = models.FloatField(default=0.0, help_text="Consumo actual (simulado)")
    voltaje_operacion = models.FloatField(default=220.0)
    frecuencia = models.FloatField(default=50.0, help_text="Frecuencia de operación (Hz)")
    estado = models.CharField(
        max_length=20,
        default="desconectada",
        choices=[
            ("desconectada", "Desconectada"),
            ("conectada", "Conectada"),
            ("operativa", "Operativa"),
            ("sobrecarga", "Sobrecarga")
        ]
    )
    controlable = models.BooleanField(default=True, help_text="Puede encenderse/apagarse por software")
    prioridad = models.IntegerField(default=1, help_text="Prioridad para conexión si hay recursos limitados")

    def __str__(self):
        return f"{self.nombre} ({self.estado})"
