
# Módulo para definir requisitos energéticos y estructuras funcionales

# Costos aproximados de operaciones (en kW)
COSTO_CREAR_CELULA = 5.0
COSTO_EVOLUCION = 2.0
COSTO_MANTENIMIENTO = 0.2

# Requisitos para que un tipo de organulo funcione (por tipo)
# Indica la energía mínima requerida y los organulos que deben estar activos
REQUISITOS_ORGANULOS = {
    "O4": {
        "energia_minima": 5.0,
        "dependencias": ["O3-1", "O3-2", "O3-3", "O3-4", "O3-5"]
    },
    "O3": {
        "energia_minima": 1.0,
        "dependencias_por_pares": [["O1-1", "O1-2"], ["O1-3", "O1-4"], ["O1-5", "O1-6"], ["O1-7", "O1-8"], ["O1-9", "O1-10"]]
    },
    "O2": {
        "energia_minima": 0.5,
        "dependencias": ["O1-0"]
    }
}

# Validar si una célula tiene estructura completa para evolución
def celula_puede_evolucionar(celula, organulos):
    energia = celula.get("energia_actual", 0)
    if energia < COSTO_CREAR_CELULA:
        return False

    ids_activos = set([o["id"] for o in organulos if o["celula_asociada"] == celula["id"] and o.get("estado") in ["activo", "operativo"]])

    # Validar requisitos de organulo O4 como núcleo
    requisitos = REQUISITOS_ORGANULOS.get("O4")
    if not requisitos:
        return True

    if energia < requisitos["energia_minima"]:
        return False

    if not all(dep in ids_activos for dep in requisitos["dependencias"]):
        return False

    return True
