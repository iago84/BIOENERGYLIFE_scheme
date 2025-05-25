class Generador:
    def __init__(self, id, tipo, potencia_kw, rpm_min, voltaje_salida_v, eficiencia, aplicacion):
        self.id = id
        self.tipo = tipo
        self.potencia_kw = potencia_kw
        self.rpm_min = rpm_min
        self.voltaje_salida_v = voltaje_salida_v
        self.eficiencia = eficiencia
        self.aplicacion = aplicacion

    def info(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "potencia_kw": self.potencia_kw,
            "rpm_min": self.rpm_min,
            "voltaje_salida_v": self.voltaje_salida_v,
            "eficiencia": self.eficiencia,
            "aplicacion": self.aplicacion
        }

    def energia_entregada(self, carga=1.0):
        return round(self.potencia_kw * self.eficiencia * carga, 3)
