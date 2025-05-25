class Generador:
    def __init__(self, id, tipo, potencia_kw, rpm_min, voltaje_salida_v, eficiencia, aplicacion, arranques=None, notas=""):
        self.id = id
        self.tipo = tipo
        self.potencia_kw = potencia_kw
        self.rpm_min = rpm_min
        self.voltaje_salida_v = voltaje_salida_v
        self.eficiencia = eficiencia
        self.aplicacion = aplicacion
        self.arranques = arranques or []
        self.notas = notas

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "potencia_kw": self.potencia_kw,
            "rpm_min": self.rpm_min,
            "voltaje_salida_v": self.voltaje_salida_v,
            "eficiencia": self.eficiencia,
            "aplicacion": self.aplicacion,
            "arranques": self.arranques,
            "notas": self.notas
        }

    @classmethod
    def from_dict(cls, d):
        return cls(**d)
