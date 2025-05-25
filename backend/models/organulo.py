class Organulo:
    def __init__(self, id, codigo, potencia, tipo="", celula_id=None, estado="inactivo", atributos=None):
        self.id = id                  # ID único para el organulo (string o int)
        self.codigo = codigo          # Código tipo "O1", "O2", etc.
        self.potencia = potencia      # Potencia en kW
        self.tipo = tipo              # Tipo: "mitocondria", "ribosoma", etc. (si aplica)
        self.celula_id = celula_id    # ID de la célula a la que pertenece (opcional)
        self.estado = estado          # "activo", "inactivo", etc.
        self.atributos = atributos or {}  # Extras flexibles

    def operar(self):
        return f"Órgánulo {self.codigo} ({self.tipo}) operando con {self.potencia}kW"

    def to_dict(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "potencia": self.potencia,
            "tipo": self.tipo,
            "celula_id": self.celula_id,
            "estado": self.estado,
            "atributos": self.atributos
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            id=d.get("id"),
            codigo=d.get("codigo"),
            potencia=d.get("potencia"),
            tipo=d.get("tipo", ""),
            celula_id=d.get("celula_id"),
            estado=d.get("estado", "inactivo"),
            atributos=d.get("atributos", {})
        )
