
from db import generadores_table

def obtener_generador_por_aplicacion(tipo_org):
    # Buscar generador compatible con tipo de orgánulo
    gen = generadores_table.get(lambda g: g["aplicacion"] == tipo_org)
    return gen or {}

def potencia_neta(disponible_kw, eficiencia):
    return disponible_kw * eficiencia

def puede_activar_generador(organulo, energia_celula, rpm_actual):
    tipo = organulo["tipo"]
    gen = obtener_generador_por_aplicacion(tipo)
    if not gen:
        return False

    # Verificaciones básicas
    if energia_celula < gen["potencia_kw"]:
        return False
    if rpm_actual < gen["rpm_min"]:
        return False

    return True

def energia_generada_por(organulo, energia_celula, rpm):
    gen = obtener_generador_por_aplicacion(organulo["tipo"])
    if not gen:
        return 0

    if energia_celula < gen["potencia_kw"] or rpm < gen["rpm_min"]:
        return 0

    return potencia_neta(gen["potencia_kw"], gen["eficiencia"])


# === FUNCIONES DE CALCULO DE NECESIDADES Y PRODUCCIÓN ===
def calcular_necesidad_arranque(celula):
    total = 0
    for o_id in celula.get("organulos", []):
        o = organulos_table.get(lambda x: x["id"]==o_id)
        if o: total += o.get("potencia", 0)
    return total

def calcular_produccion(celula):
    return sum([
        o.get("potencia", 0) for o in [organulos_table.get(lambda x: x["id"]==oid) for oid in celula.get("organulos",[])]
        if o and o.get("estado","")=="operativo"
    ])
