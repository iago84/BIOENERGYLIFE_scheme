from django.db import models


class TipoMotor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    tecnologia = models.CharField(max_length=50, default="DC")  # Ej: 'AC', 'DC', 'Brushless', etc.

    def __str__(self):
        return self.nombre


class Motor(models.Model):
    nombre = models.CharField(max_length=100, default="")
    tipo = models.CharField(max_length=50, default="indefinido")  # Puedes usarlo como identificador adicional
    tipo_motor = models.ForeignKey(TipoMotor, on_delete=models.SET_NULL, null=True, blank=True)

    potencia_nominal_kw = models.FloatField(default=0.0)
    rpm_nominal = models.FloatField(default=0.0)
    corriente_nominal = models.FloatField(default=0.0)
    voltaje_operacion_v = models.FloatField(default=0.0)
    eficiencia = models.FloatField(default=0.9)

    consumo_arranque_kw = models.FloatField(default=0.0)
    ciclos_vida = models.IntegerField(default=10000)

    estado = models.CharField(
        max_length=20,
        choices=[("operativo", "Operativo"), ("mantenimiento", "Mantenimiento"), ("fallo", "Fallo")],
        default="operativo"
    )

    firmware_version = models.CharField(max_length=20, blank=True, null=True)
    config_extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.nombre
