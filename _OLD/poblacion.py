
from db import generadores_table, config_table, celulas_table, organulos_table, tejidos_table, organos_table

def poblar_generadores_y_config():
    generadores_table.truncate()
    config_table.truncate()

    generadores = [
        {"id": "G-M100", "nombre": "Micro Generador Manual", "tipo": "iman_fijo", "potencia_kw": 0.1, "rpm_min": 60, "voltaje_salida_v": 12, "eficiencia": 0.75, "aplicacion": "O1"},
        {"id": "G-I1K", "nombre": "Generador Inducción 1kW", "tipo": "induccion", "potencia_kw": 1.0, "rpm_min": 250, "voltaje_salida_v": 48, "eficiencia": 0.88, "aplicacion": "O3"},
        {"id": "G-I5K", "nombre": "Generador Inducción 5kW", "tipo": "induccion", "potencia_kw": 5.0, "rpm_min": 500, "voltaje_salida_v": 220, "eficiencia": 0.91, "aplicacion": "O4"}
    ]
    generadores_table.insert_multiple(generadores)

    config_table.insert_multiple([
        {"clave": "velocidad_simulacion", "valor": 1.0},
        {"clave": "energia_inicial", "valor": 10},
        {"clave": "ciclos_maximos", "valor": 1000}
    ])

def crear_celula_germinadora(id, tipo_arranque, ubicacion, madre=None):
    orgs = []
    org_ids = []

    if tipo_arranque in ["manual", "mixta"]:
        orgs.append({"id": f"{id}-O0", "tipo": "O0", "potencia": 5.0, "estado": "manual", "celula_asociada": id})
        org_ids.append(f"{id}-O0")
    if tipo_arranque in ["solar", "mixta"]:
        orgs.append({"id": f"{id}-O11", "tipo": "O11", "potencia": 0.1, "estado": "pasivo", "celula_asociada": id})
        org_ids.append(f"{id}-O11")

    organulos_table.insert_multiple(orgs)

    celulas_table.insert({
        "id": id,
        "tipo": "G",
        "energia_actual": 0.0,
        "energia_maxima": 10,
        "organulos": org_ids,
        "estado": "activa",
        "ubicacion": ubicacion,
        "nivel_evolucion": 1,
        "enlaces": [],
        "generada_por": madre,
        "puede_multiplicar": True,
        "posibles_evoluciones": ["CEA", "CST", "CFB", "CVP"]
    })

def poblar_red_inicial_expandida():
    celulas_table.truncate()
    organulos_table.truncate()
    tejidos_table.truncate()
    organos_table.truncate()

    poblar_generadores_y_config()

    crear_celula_germinadora("CG1", "solar", {"x": 100, "y": 100})
    crear_celula_germinadora("CG2", "manual", {"x": 300, "y": 100})
    crear_celula_germinadora("CG3", "mixta", {"x": 500, "y": 100})
    crear_celula_germinadora("CG4", "madre", {"x": 700, "y": 100}, madre="CG3")

    print("Células germinadoras CG1–CG4 generadas con orgánulos O0/O11.")
