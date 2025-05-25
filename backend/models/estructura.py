class Tejido:
    def __init__(self, id, tipo, celulas, funcion, nodo_destino, atributos=None):
        self.id = id  # ID único
        self.tipo = tipo  # Ej: "muscular", "conector", etc.
        self.celulas = celulas  # Lista de IDs o de objetos Celula (ideal: IDs para BD)
        self.funcion = funcion  # Descripción funcional
        self.nodo_destino = nodo_destino  # Nodo/órgano al que conecta
        self.atributos = atributos or {}  # Extensible, cualquier cosa (color, meta, etc.)

    def descripcion(self):
        return (f"Tejido {self.tipo} (ID: {self.id}) con {len(self.celulas)} células "
                f"destinado a {self.nodo_destino}")

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "celulas": self.celulas,
            "funcion": self.funcion,
            "nodo_destino": self.nodo_destino,
            "atributos": self.atributos
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            id=d.get("id"),
            tipo=d.get("tipo"),
            celulas=d.get("celulas", []),
            funcion=d.get("funcion", ""),
            nodo_destino=d.get("nodo_destino", ""),
            atributos=d.get("atributos", {})
        )


class Organo:
    def __init__(self, id, tipo, energia_in, energia_out, estado, asociados, atributos=None):
        self.id = id  # ID único
        self.tipo = tipo  # Ej: "CP", "CD", "CRE", etc.
        self.energia_in = energia_in  # kW de entrada
        self.energia_out = energia_out  # kW de salida
        self.estado = estado  # "activo", "dañado", "latente", etc.
        self.asociados = asociados  # IDs de órganos, tejidos o células asociados
        self.atributos = atributos or {}  # Para cualquier extra

    def rendimiento(self):
        if self.energia_in == 0:
            return 0
        return round(self.energia_out / self.energia_in, 3)

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "energia_in": self.energia_in,
            "energia_out": self.energia_out,
            "estado": self.estado,
            "asociados": self.asociados,
            "atributos": self.atributos
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            id=d.get("id"),
            tipo=d.get("tipo"),
            energia_in=d.get("energia_in", 0),
            energia_out=d.get("energia_out", 0),
            estado=d.get("estado", "inactivo"),
            asociados=d.get("asociados", []),
            atributos=d.get("atributos", {})
        )
