# migrar_y_corregir_bd.py
from uuid import uuid4

from backend.db import celulas_table, organulos_table

LOG = []

def corregir_celula(cel):
    changed = False
    # Energia actual y maxima
    if "energia_actual" not in cel:
        old = cel.get("energia", 0)
        cel["energia_actual"] = old
        changed = True
        LOG.append(f"[CORREGIDO] {cel['id']}: añadido 'energia_actual' (valor {old})")
    if "energia_maxima" not in cel:
        cel["energia_maxima"] = 10
        changed = True
        LOG.append(f"[CORREGIDO] {cel['id']}: añadido 'energia_maxima' (valor 10)")
    # Estado
    if "estado" not in cel:
        cel["estado"] = "activa"
        changed = True
        LOG.append(f"[CORREGIDO] {cel['id']}: añadido 'estado' (activa)")
    # Organulos
    if "organulos" not in cel or not isinstance(cel["organulos"], list):
        cel["organulos"] = []
        changed = True
        LOG.append(f"[CORREGIDO] {cel['id']}: añadido campo 'organulos' (lista vacía)")
    # Ubicación
    if "ubicacion" not in cel or not isinstance(cel["ubicacion"], dict):
        cel["ubicacion"] = {"x": 100, "y": 100}
        changed = True
        LOG.append(f"[CORREGIDO] {cel['id']}: añadido campo 'ubicacion'")
    # Nivel de evolución
    if "nivel_evolucion" not in cel:
        cel["nivel_evolucion"] = 1
        changed = True
        LOG.append(f"[CORREGIDO] {cel['id']}: añadido campo 'nivel_evolucion'")
    # Enlaces
    if "enlaces" not in cel or not isinstance(cel["enlaces"], list):
        cel["enlaces"] = []
        changed = True
        LOG.append(f"[CORREGIDO] {cel['id']}: añadido campo 'enlaces' (lista vacía)")
    # Ciclos activada
    if "ciclos_activada" not in cel:
        cel["ciclos_activada"] = 0
        changed = True
        LOG.append(f"[CORREGIDO] {cel['id']}: añadido campo 'ciclos_activada' (0)")

    # Verifica condiciones de arranque: Germinadoras deben tener O0 (manual) u O11 (solar)
    if cel["tipo"] == "G":
        organulos = [o for o in organulos_table.all() if o["celula_asociada"] == cel["id"]]
        ids = [o["tipo"] for o in organulos]
        creado = False
        if "O0" not in ids and "O11" not in ids:
            # Crea orgánulo O11 (solar) por defecto si ninguno
            o_id = cel["id"] + "-O11"
            organulos_table.insert({
                "id": o_id, "tipo": "O11", "potencia": 0.5, "estado": "pasivo", "celula_asociada": cel["id"]
            })
            cel["organulos"].append(o_id)
            creado = True
            LOG.append(f"[ARRANQUE] {cel['id']}: añadido orgánulo de arranque O11 (solar)")
        elif "O0" not in ids:
            # Opcionalmente, crea O0 si quieres siempre doble arranque
            pass
        if not creado:
            # Sincroniza organulo_ids con la tabla por si hay desajustes
            cel["organulos"] = [o["id"] for o in organulos if o["celula_asociada"] == cel["id"]]

    # Más tipos personalizados pueden añadirse aquí...

    return cel, changed

def main():
    print("== MIGRADOR SIMULADOR ORGÁNICO ==")
    cels = celulas_table.all()
    n_corr = 0
    for cel in cels:
        cel_corr, changed = corregir_celula(cel)
        if changed:
            celulas_table.update(cel_corr, lambda c: c["id"] == cel_corr["id"])
            n_corr += 1
    print(f"Total células corregidas: {n_corr}")
    for l in LOG:
        print(l)
    print("[INFO] Ejecución completada.")

if __name__ == "__main__":
    main()
