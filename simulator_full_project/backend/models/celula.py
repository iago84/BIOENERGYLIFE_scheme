class Celula:
    def __init__(self, tipo, energia):
        self.tipo = tipo
        self.energia = energia

    def activar(self):
        return f"Célula tipo {self.tipo} activada con {self.energia}kW"

    def mutar(self, nuevo_tipo):
        self.tipo = nuevo_tipo
        return f"Célula ha mutado a tipo {self.tipo}"

    def fusionar(self, otra):
        self.energia += otra.energia
        return f"Fusión completada, energía total: {self.energia}kW"