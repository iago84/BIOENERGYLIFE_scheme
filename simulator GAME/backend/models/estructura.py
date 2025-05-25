class Tejido:
    def __init__(self, id, tipo, celulas, funcion, nodo_destino):
        self.id = id
        self.tipo = tipo
        self.celulas = celulas
        self.funcion = funcion
        self.nodo_destino = nodo_destino

    def descripcion(self):
        return f"Tejido {self.tipo} con {len(self.celulas)} células destinado a {self.nodo_destino}"

class Organo:
    def __init__(self, id, tipo, energia_in, energia_out, estado, asociados):
        self.id = id
        self.tipo = tipo
        self.energia_in = energia_in
        self.energia_out = energia_out
        self.estado = estado
        self.asociados = asociados

    def rendimiento(self):
        if self.energia_in == 0:
            return 0
        return round(self.energia_out / self.energia_in, 3)
