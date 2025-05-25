# parche_realismo.py
"""
Módulo para añadir realismo físico y visual al ciclo energético.
Incluye:
- Cálculo realista de consumo y generación (eficiencia, pérdidas)
- Validación física de generadores vs carga
- Balanceo de racks
- Corrección de superposición de nodos para frontend (canvas)
"""

def calcular_consumo_total(celula, acciones=None):
    """
    Calcula el consumo total de una célula para un ciclo:
    - Consumo base de supervivencia
    - Consumo por acción (crear, evolucionar, reparar...)
    """
    if acciones is None:
        acciones = []
    consumo = celula.get("consumo_kw", 0)
    for accion in acciones:
        if accion == "crear":
            consumo += 5.0  # kW (ejemplo)
        elif accion == "evolucionar":
            consumo += 2.0
        elif accion == "reparar":
            consumo += 1.5
    return consumo


def calcular_generacion_total(celula, organulos, generadores, eficiencia_base=0.85, perdidas=0.05):
    """
    Calcula la energía generada por una célula en un ciclo:
    - Suma potencia de orgánulos activos y generadores físicos asociados
    - Aplica eficiencia y pérdidas
    """
    energia = 0
    for oid in celula.get("organulos", []):
        org = next((o for o in organulos if o["id"] == oid), None)
        if org and org.get("estado") in ("activo", "operativo"):
            energia += org.get("potencia", 0)
    # Generadores físicos (si la célula está asociada)
    if "generadores" in celula:
        for gid in celula["generadores"]:
            gen = next((g for g in generadores if g["id"] == gid), None)
            if gen:
                energia += gen["potencia_kw"] * gen.get("eficiencia", 0.85)
    energia = energia * eficiencia_base * (1 - perdidas)
    return energia


def validar_generador_vs_consumo(generador, celulas_asociadas):
    """
    Comprueba si el generador soporta la suma de consumos de las células que alimenta.
    Devuelve (bool, consumo_total).
    """
    consumo_total = sum(c.get("consumo_kw", 0) for c in celulas_asociadas)
    max_pot = generador["potencia_kw"] * generador.get("eficiencia", 0.85)
    if consumo_total > max_pot:
        return False, consumo_total
    return True, consumo_total


def balancear_rack(generadores, celulas):
    """
    Distribuye el consumo entre generadores (ejemplo: reparto proporcional simple).
    Si no hay suficiente potencia total, reduce consumo de todas.
    """
    consumos = [c.get("consumo_kw", 0) for c in celulas]
    potencias = [g["potencia_kw"] * g.get("eficiencia", 0.85) for g in generadores]
    total_consumo = sum(consumos)
    total_potencia = sum(potencias)
    if total_consumo > total_potencia:
        factor = total_potencia / total_consumo
        for c in celulas:
            c["consumo_kw"] *= factor
        return False, factor  # Hay limitación, consumos reducidos
    return True, 1.0  # Todo ok


def corregir_superposiciones(celulas, min_distancia=50):
    """
    Ajusta posiciones de las células para evitar superposición visual (canvas).
    Modifica las posiciones in place.
    """
    for i, c1 in enumerate(celulas):
        for j, c2 in enumerate(celulas):
            if i >= j:
                continue
            dx = c1["ubicacion"]["x"] - c2["ubicacion"]["x"]
            dy = c1["ubicacion"]["y"] - c2["ubicacion"]["y"]
            dist = (dx**2 + dy**2)**0.5
            if dist < min_distancia and dist > 0:
                mov = (min_distancia - dist) / 2
                # Separa ambos nodos
                norm = (dx**2 + dy**2)**0.5 or 1
                c1["ubicacion"]["x"] += int(mov * dx / norm)
                c1["ubicacion"]["y"] += int(mov * dy / norm)
                c2["ubicacion"]["x"] -= int(mov * dx / norm)
                c2["ubicacion"]["y"] -= int(mov * dy / norm)
    return celulas  # Por si quieres encadenar

# Opcional: función para visualizar el estado de racks
def info_racks(racks, generadores, celulas):
    """
    Da información resumen para visualización de racks, generadores y su carga.
    """
    out = []
    for rack in racks:
        gens = [g for g in generadores if g["id"] in rack["generadores"]]
        cels = [c for c in celulas if c["id"] in rack["celulas"]]
        ok, factor = balancear_rack(gens, cels)
        out.append({
            "rack_id": rack["id"],
            "generadores": [g["id"] for g in gens],
            "celulas": [c["id"] for c in cels],
            "total_consumo": sum(c.get("consumo_kw", 0) for c in cels),
            "total_potencia": sum(g["potencia_kw"] for g in gens),
            "factor_balanceo": factor,
            "sobrecarga": not ok
        })
    return out

# ----------- INTEGRACIÓN EN CICLO DE EVOLUCIÓN -------------

def evolucionar_realista(celulas, organulos, generadores, acciones_por_celula=None, eficiencia_base=0.85, perdidas=0.05):
    """
    Ejemplo de ciclo de evolución que usa los nuevos cálculos.
    Modifica directamente las energías y estados.
    """
    resultados = []
    if acciones_por_celula is None:
        acciones_por_celula = {}
    for cel in celulas:
        acciones = acciones_por_celula.get(cel["id"], [])
        consumo = calcular_consumo_total(cel, acciones)
        generacion = calcular_generacion_total(cel, organulos, generadores, eficiencia_base, perdidas)
        energia_actual = cel.get("energia_actual", 0)
        energia_maxima = cel.get("energia_maxima", 10)
        nueva_energia = max(0, min(energia_actual + generacion - consumo, energia_maxima))
        cel["energia_actual"] = nueva_energia
        if generacion < consumo:
            resultados.append(f"{cel['id']}: sin energía suficiente para ciclo (consumo={consumo:.2f}, gen={generacion:.2f})")
        else:
            resultados.append(f"{cel['id']}: activada (gen={generacion:.2f}, consumo={consumo:.2f}, energia={nueva_energia:.2f})")
        # Puedes aquí activar/mutar/crear células según energía
    return resultados

# -----------------------------------------------------------
