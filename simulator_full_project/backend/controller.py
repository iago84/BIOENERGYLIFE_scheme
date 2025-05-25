from db import celulas_table, logs_table
from logger import log_event

def cargar_inicial():
    # Aquí no se necesita reiniciar nada si ya hay una red cargada
    if len(celulas_table.all()) == 0:
        from poblacion import poblar_red_inicial
        poblar_red_inicial()
    log_event("sistema", "Red energética germinadora cargada", "sistema")

def evolucionar(ciclos=1):
    resultados = []
    for ciclo in range(ciclos):
        log_event("ciclo", f"== CICLO {ciclo + 1} ==", f"ciclo-{ciclo + 1}")
        celulas = celulas_table.all()

        for cel in celulas:
            if cel["energia_actual"] >= 1:
                cel["energia_actual"] -= 1  # costo por activación
                for target_id in cel.get("enlaces", []):
                    target = celulas_table.get(doc_id=target_id) if isinstance(target_id, int) else celulas_table.get(lambda x: x["id"] == target_id)
                    if target:
                        target["energia_actual"] += 1
                        celulas_table.update({"energia_actual": target["energia_actual"]}, doc_ids=[target.doc_id])
                        log_event("transferencia", f"{cel['id']} transfirió energía a {target['id']}", cel["id"])
                celulas_table.update({"energia_actual": cel["energia_actual"]}, doc_ids=[cel.doc_id])
                resultados.append(f"{cel['id']} activada con éxito")
                log_event("activacion", f"{cel['id']} activada", cel["id"])
            else:
                resultados.append(f"{cel['id']} no tiene energía suficiente")
                log_event("fallo", f"{cel['id']} no pudo activarse por falta de energía", cel["id"])

    return resultados
