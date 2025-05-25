class Celula:
    def __init__(self, id, tipo, energia, organulos=None, estado="inactiva", generacion=1,
                 atributos=None, estable=None, productiva=None, consumo_kw=0, produccion_kw=0,
                 energia_maxima=10, historial=None):
        self.id = id
        self.tipo = tipo
        self.energia = energia
        self.organulos = organulos or []  # IDs o dicts de orgánulos
        self.estado = estado
        self.generacion = generacion
        self.atributos = atributos or {}
        self.estable = estable  # True/False/None
        self.productiva = productiva  # True/False/None
        self.consumo_kw = consumo_kw  # Energía mínima para vivir
        self.produccion_kw = produccion_kw  # Potencia máxima producida
        self.energia_maxima = energia_maxima
        self.historial = historial or []

    def activar(self):
        self.estado = "activa"
        self.historial.append(f"Activada con {self.energia}kW")
        return f"Célula {self.id} de tipo {self.tipo} activada con {self.energia}kW"

    def mutar(self, nuevo_tipo):
        self.tipo = nuevo_tipo
        self.generacion += 1
        self.historial.append(f"Mutó a tipo {self.tipo}")
        return f"Célula {self.id} ha mutado a tipo {self.tipo} (gen {self.generacion})"

    def fusionar(self, otra):
        energia_antes = self.energia
        self.energia += otra.energia
        self.historial.append(f"Fusión: absorbió {otra.energia}kW de célula {getattr(otra, 'id', 'desconocida')}")
        return (f"Fusión completada: célula {self.id} absorbió {otra.energia}kW de célula {getattr(otra, 'id', 'desconocida')}. "
                f"Energía total: {energia_antes} + {otra.energia} = {self.energia}kW")

    def es_estable(self):
        # Ejemplo: estable si energía > consumo y todos los orgánulos están activos
        if self.energia < self.consumo_kw:
            return False
        if any(org.get('estado', 'inactivo') != 'operativo' for org in self.organulos if isinstance(org, dict)):
            return False
        return True

    def es_productiva(self):
        # Ejemplo: productiva si energía > producción mínima y tiene algún orgánulo de tipo productor activo
        if self.energia < self.produccion_kw:
            return False
        productores = [org for org in self.organulos if (isinstance(org, dict) and org.get('tipo') in ['O3', 'O4'] and org.get('estado') == 'operativo')]
        return len(productores) > 0

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "energia": self.energia,
            "organulos": self.organulos,
            "estado": self.estado,
            "generacion": self.generacion,
            "atributos": self.atributos,
            "estable": self.estable,
            "productiva": self.productiva,
            "consumo_kw": self.consumo_kw,
            "produccion_kw": self.produccion_kw,
            "energia_maxima": self.energia_maxima,
            "historial": self.historial
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            id=d.get("id"),
            tipo=d.get("tipo"),
            energia=d.get("energia"),
            organulos=d.get("organulos", []),
            estado=d.get("estado", "inactiva"),
            generacion=d.get("generacion", 1),
            atributos=d.get("atributos", {}),
            estable=d.get("estable"),
            productiva=d.get("productiva"),
            consumo_kw=d.get("consumo_kw", 0),
            produccion_kw=d.get("produccion_kw", 0),
            energia_maxima=d.get("energia_maxima", 10),
            historial=d.get("historial", [])
        )
