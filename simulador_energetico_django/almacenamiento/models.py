from django.db import models

class TipoReserva(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tecnologia = models.CharField(
        max_length=50,
        default="batería",
        help_text="Tipo de tecnología: batería, volante de inercia, supercondensador, etc."
    )
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class ReservaEnergetica(models.Model):
    nombre = models.CharField(max_length=100, default="")
    tipo = models.CharField(max_length=50, default="batería")
    tipo_reserva = models.ForeignKey(TipoReserva, on_delete=models.SET_NULL, null=True, blank=True)

    capacidad_actual_kw = models.FloatField(default=0.0, help_text="Cantidad actual de energía almacenada (kW)")
    capacidad_max_kw = models.FloatField(default=0.0, help_text="Capacidad máxima de almacenamiento (kW)")
    ciclos_vida = models.IntegerField(default=1000)
    estado = models.CharField(
        max_length=20,
        default="disponible",
        choices=[("disponible", "Disponible"), ("descargando", "Descargando"), ("cargando", "Cargando"), ("agotada", "Agotada")]
    )
    fecha_instalacion = models.DateField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)

    def porcentaje_carga(self):
        if self.capacidad_max_kw > 0:
            return round(100 * self.capacidad_actual_kw / self.capacidad_max_kw, 2)
        return 0.0

    def __str__(self):
        return f"{self.nombre} ({self.porcentaje_carga()}%)"
