from db import generadores_table, config_table, celulas_table, organulos_table, tejidos_table, organos_table

def poblar_generadores():
    generadores_table.truncate()
    generadores = [
        {"id": "G-M100", "nombre": "Micro Generador Manual", "tipo": "iman_fijo", "potencia_kw": 0.1, "rpm_min": 60, "voltaje_salida_v": 12, "eficiencia": 0.75, "aplicacion": "O1"},
        {"id": "G-I1K", "nombre": "Generador Inducción 1kW", "tipo": "induccion", "potencia_kw": 1.0, "rpm_min": 250, "voltaje_salida_v": 48, "eficiencia": 0.88, "aplicacion": "O3"},
        {"id": "G-I5K", "nombre": "Generador Inducción 5kW", "tipo": "induccion", "potencia_kw": 5.0, "rpm_min": 500, "voltaje_salida_v": 220, "eficiencia": 0.91, "aplicacion": "O4"}
    ]
    generadores_table.insert_multiple(generadores)

def poblar_configuracion():
    config_table.truncate()
    config_table.insert_multiple([
        {"clave": "velocidad_simulacion", "valor": 1.0},
        {"clave": "energia_inicial", "valor": 10},
        {"clave": "ciclos_maximos", "valor": 1000}
    ])

def crear_celula_germinadora(celula_id, posicion={"x": 0, "y": 0}):
    organulos = []

    # O1 inicial manual
    organulos.append({"id": f"{celula_id}-O1-0", "tipo": "O1", "potencia": 0.1, "estado": "operativo", "celula_asociada": celula_id,
                      "activa_a": [f"{celula_id}-O1-" + str(i) for i in range(1, 11)], "depende_de": [], "secuenciador": True})

    # O1 secundarios
    for i in range(1, 11):
        organulos.append({"id": f"{celula_id}-O1-{i}", "tipo": "O1", "potencia": 0.1, "estado": "espera", "celula_asociada": celula_id,
                          "activa_a": [], "depende_de": [f"{celula_id}-O1-0"], "secuenciador": False})

    # O3 motores
    for i in range(1, 6):
        organulos.append({"id": f"{celula_id}-O3-{i}", "tipo": "O3", "potencia": 1.0, "estado": "espera", "celula_asociada": celula_id,
                          "activa_a": [f"{celula_id}-O4-1"], "depende_de": [f"{celula_id}-O1-" + str(i * 2 - 1), f"{celula_id}-O1-" + str(i * 2)], "secuenciador": False})

    # O4 generador
    organulos.append({"id": f"{celula_id}-O4-1", "tipo": "O4", "potencia": 5.0, "estado": "espera", "celula_asociada": celula_id,
                      "activa_a": [], "depende_de": [f"{celula_id}-O3-{i}" for i in range(1, 6)], "secuenciador": False})

    organulos_table.insert_multiple(organulos)

    celulas_table.insert({
        "id": celula_id,
        "tipo": "G",
        "energia_actual": 0.5,
        "energia_maxima": 10,
        "organulos": [o["id"] for o in organulos],
        "estado": "activa",
        "ubicacion": posicion,
        "nivel_evolucion": 1,
        "enlaces": [],
        "generada_por": None,
        "puede_multiplicar": True
    })

def poblar_red_inicial():
    poblar_generadores()
    poblar_configuracion()
    crear_celula_germinadora("C1")
