from django.db import models

class Simulacion(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    parametros = models.JSONField(blank=True, null=True)
    estado = models.CharField(max_length=20, default="en_progreso")
    def __str__(self):
        return getattr(self, "nombre", f"Simulacion {self.pk}")


class ResultadoSimulacion(models.Model):
    simulacion = models.ForeignKey("Simulacion", on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    resultados = models.JSONField(blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    def __str__(self):
        return getattr(self, "nombre", f"ResultadoSimulacion {self.pk}")
