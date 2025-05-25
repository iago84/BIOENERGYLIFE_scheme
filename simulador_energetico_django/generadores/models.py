from django.db import models

class TipoGenerador(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    tecnologia = models.CharField(max_length=50, default="iman_fijo")  # Ej: 'iman_fijo', 'induccion', 'solar', etc.

    def __str__(self):
        return self.nombre

class Generador(models.Model):
    nombre = models.CharField(max_length=100, default="")
    tipo = models.CharField(max_length=50, default="indefinido")  # Relaciona con TipoGenerador si quieres ForeignKey
    tipo_generador = models.ForeignKey(TipoGenerador, on_delete=models.SET_NULL, null=True, blank=True)
    potencia_nominal_kw = models.FloatField(default=0.0)
    eficiencia = models.FloatField(default=1.0)
    rpm_min = models.FloatField(default=0.0)
    rpm_max = models.FloatField(default=0.0)
    # En Generador
    voltaje_entrada_v = models.FloatField(
        default=0.0,
        help_text="Voltaje de entrada requerido para el arranque o excitación (V)"
    )

    # Opcional, para Arranque si necesitas por cada método:
    voltaje_entrada_requerido_v = models.FloatField(
        default=0.0,
        help_text="Voltaje mínimo necesario para este arranque"
    )

    voltaje_salida_v = models.FloatField(default=0.0)
    aplicacion = models.CharField(max_length=50, blank=True, null=True)
    estado_funcional = models.CharField(
        max_length=50,
        choices=[("operativo", "Operativo"), ("parado", "Parado"), ("error", "Error")],
        default="operativo"
    )
    puede_arrancar = models.BooleanField(default=True)
    consumo_arranque_kw = models.FloatField(default=0.0, help_text="Consumo específico en arranque (kW)")
    tension_minima = models.FloatField(default=0.0, help_text="Tensión mínima de operación")
    firmware_version = models.CharField(max_length=20, blank=True, null=True)
    arranques_disponibles = models.JSONField(blank=True, null=True, help_text="Opciones de arranque")
    config_extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Arranque(models.Model):
    generador = models.ForeignKey(Generador, on_delete=models.CASCADE, related_name='arranques', blank=True, null=True)
    tipo_arranque = models.CharField(
        max_length=30,
        choices=[
            ("manual", "Manual"),
            ("motor_aux", "Motor Auxiliar"),
            ("corriente_externa", "Corriente Externa"),
            ("solar", "Solar"),
            ("hidraulico", "Hidráulico")
        ],
        default="manual"
    )
    costo_arranque_kw = models.FloatField(default=0.0)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_arranque} ({self.generador.nombre if self.generador else 'Sin Generador'})"

class Rack(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    generadores = models.ManyToManyField(Generador, blank=True, related_name='racks')
    capacidad_kw = models.FloatField(default=0.0)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=[("operativo", "Operativo"), ("mantenimiento", "Mantenimiento"), ("fallo", "Fallo")],
        default="operativo"
    )

    def __str__(self):
        return self.nombre
