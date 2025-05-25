class Organulo:
    def __init__(self, codigo, potencia):
        self.codigo = codigo
        self.potencia = potencia

    def operar(self):
        return f"Órgánulo {self.codigo} operando con {self.potencia}kW"