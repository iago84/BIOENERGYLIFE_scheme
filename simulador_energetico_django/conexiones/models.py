from django.db import models

class TipoConexion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(
        max_length=50,
        choices=[
            ("energética", "Energética"),
            ("control", "Control"),
            ("información", "Información"),
            ("sináptica", "Sináptica")
        ],
        default="energética"
    )

    def __str__(self):
        return self.nombre


class Conexion(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tipo_conexion = models.CharField(
        max_length=20,
        choices=[
            ("energética", "Energética"),
            ("control", "Control"),
            ("información", "Información"),
            ("sináptica", "Sináptica")
        ],
        default="energética"
    )
    tipo = models.ForeignKey(TipoConexion, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        default="activa",
        choices=[
            ("activa", "Activa"),
            ("inactiva", "Inactiva"),
            ("fallo", "Fallo")
        ]
    )
    ancho_banda_kw = models.FloatField(default=0.0, help_text="Máximo flujo permitido si aplica (kW)")
    metadata = models.JSONField(blank=True, null=True, help_text="Información adicional para simulación")

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.tipo_conexion})"
