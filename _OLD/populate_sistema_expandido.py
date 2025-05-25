
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

def crear_celula_tecnica():
    organulos = []

    organulos.append({"id": "O1-0", "tipo": "O1", "potencia": 0.1, "estado": "operativo", "celula_asociada": "C1", "activa_a": ["O1-" + str(i) for i in range(1, 11)], "depende_de": [], "secuenciador": True})

    for i in range(1, 11):
        organulos.append({"id": f"O1-{i}", "tipo": "O1", "potencia": 0.1, "estado": "espera", "celula_asociada": "C1", "activa_a": [], "depende_de": ["O1-0"], "secuenciador": False})

    for i in range(1, 6):
        organulos.append({"id": f"O3-{i}", "tipo": "O3", "potencia": 1.0, "estado": "espera", "celula_asociada": "C1", "activa_a": ["O4-1"], "depende_de": ["O1-" + str(i * 2 - 1), "O1-" + str(i * 2)], "secuenciador": False})

    organulos.append({"id": "O4-1", "tipo": "O4", "potencia": 5.0, "estado": "espera", "celula_asociada": "C1", "activa_a": [], "depende_de": ["O3-1", "O3-2", "O3-3", "O3-4", "O3-5"], "secuenciador": False})

    organulos_table.insert_multiple(organulos)

    celulas_table.insert({
        "id": "C1",
        "tipo": "G",
        "energia_actual": 0.5,
        "energia_maxima": 10,
        "organulos": [o["id"] for o in organulos],
        "estado": "activa",
        "ubicacion": {"x": 0, "y": 0},
        "nivel_evolucion": 1,
        "enlaces": [],
        "generada_por": None,
        "puede_multiplicar": True,
        "posibles_evoluciones": ["CEA", "CST", "CFB", "CVP"]
    })

def crear_celula_germinadora(id, tipo_arranque, ubicacion, madre=None):
    orgs = []
    org_ids = []

    if tipo_arranque in ["manual", "mixta"]:
        o_id = f"{id}-O0"
        orgs.append({"id": o_id, "tipo": "O0", "potencia": 5.0, "estado": "manual", "celula_asociada": id})
        org_ids.append(o_id)

    if tipo_arranque in ["solar", "mixta"]:
        o_id = f"{id}-O11"
        orgs.append({"id": o_id, "tipo": "O11", "potencia": 0.5, "estado": "pasivo", "celula_asociada": id})
        org_ids.append(o_id)

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

def poblar_red_expandida():
    generadores_table.truncate()
    config_table.truncate()
    celulas_table.truncate()
    organulos_table.truncate()
    tejidos_table.truncate()
    organos_table.truncate()

    poblar_generadores_y_config()
    crear_celula_tecnica()
    crear_celula_germinadora("CG1", "solar", {"x": 100, "y": 100})
    crear_celula_germinadora("CG2", "manual", {"x": 250, "y": 100})
    crear_celula_germinadora("CG3", "mixta", {"x": 400, "y": 100})
    crear_celula_germinadora("CG4", "madre", {"x": 550, "y": 100}, madre="CG3")

    for i in range(5, 15):
        tipo = "solar" if i % 2 == 0 else "manual"
        crear_celula_germinadora(f"CG{i}", tipo, {"x": 100 + (i * 60), "y": 200})

    print("Red energética técnica y germinadora cargada.")
