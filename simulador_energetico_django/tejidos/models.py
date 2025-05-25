from django.db import models

class TipoTejido(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    nivel_estructura = models.CharField(
        max_length=50,
        choices=[
            ("básico", "Básico"),
            ("intermedio", "Intermedio"),
            ("complejo", "Complejo")
        ],
        default="básico"
    )

    def __str__(self):
        return self.nombre


class Tejido(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.ForeignKey(TipoTejido, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    celulas = models.JSONField(blank=True, null=True, help_text="IDs de células que forman el tejido")
    estado = models.CharField(
        max_length=20,
        choices=[
            ("activo", "Activo"),
            ("en_formación", "En formación"),
            ("dañado", "Dañado"),
            ("inactivo", "Inactivo")
        ],
        default="activo"
    )
    energia_total_kw = models.FloatField(default=0.0)
    productividad = models.FloatField(default=1.0, help_text="Factor multiplicador de producción o eficiencia")
    metadata = models.JSONField(blank=True, null=True, help_text="Datos adicionales: ubicación, historia, etc.")

    def __str__(self):
        return self.nombre
