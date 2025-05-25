from db import generadores_table, config_table, celulas_table, organulos_table, tejidos_table, organos_table

# Limpiar todas las tablas
generadores_table.truncate()
config_table.truncate()
celulas_table.truncate()
organulos_table.truncate()
tejidos_table.truncate()
organos_table.truncate()

# Cargar generadores base
generadores = [
    {"id": "G-M100", "nombre": "Micro Generador Manual", "tipo": "iman_fijo", "potencia_kw": 0.1, "rpm_min": 60, "voltaje_salida_v": 12, "eficiencia": 0.75, "aplicacion": "O1"},
    {"id": "G-I1K", "nombre": "Generador Inducción 1kW", "tipo": "induccion", "potencia_kw": 1.0, "rpm_min": 250, "voltaje_salida_v": 48, "eficiencia": 0.88, "aplicacion": "O3"},
    {"id": "G-I5K", "nombre": "Generador Inducción 5kW", "tipo": "induccion", "potencia_kw": 5.0, "rpm_min": 500, "voltaje_salida_v": 220, "eficiencia": 0.91, "aplicacion": "O4"}
]
generadores_table.insert_multiple(generadores)

# Configuración general
config_table.insert_multiple([
    {"clave": "velocidad_simulacion", "valor": 1.0},
    {"clave": "energia_inicial", "valor": 10},
    {"clave": "ciclos_maximos", "valor": 1000}
])

# ORGÁNULOS DE CELULA C1
organulos = []

# O1 inicial manual
organulos.append({"id": "O1-0", "tipo": "O1", "potencia": 0.1, "estado": "operativo", "celula_asociada": "C1", "activa_a": ["O1-" + str(i) for i in range(1, 11)], "depende_de": [], "secuenciador": True})

# O1 secundarios activados por secuenciador
for i in range(1, 11):
    organulos.append({"id": f"O1-{i}", "tipo": "O1", "potencia": 0.1, "estado": "espera", "celula_asociada": "C1", "activa_a": [], "depende_de": ["O1-0"], "secuenciador": False})

# O3 motores conectados a O1 secundarios
for i in range(1, 6):
    organulos.append({"id": f"O3-{i}", "tipo": "O3", "potencia": 1.0, "estado": "espera", "celula_asociada": "C1", "activa_a": ["O4-1"], "depende_de": ["O1-" + str(i * 2 - 1), "O1-" + str(i * 2)], "secuenciador": False})

# O4 generador mayor, activado por O3
organulos.append({"id": "O4-1", "tipo": "O4", "potencia": 5.0, "estado": "espera", "celula_asociada": "C1", "activa_a": [], "depende_de": ["O3-1", "O3-2", "O3-3", "O3-4", "O3-5"], "secuenciador": False})

organulos_table.insert_multiple(organulos)

# CELULA GERMINADORA C1
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
    "puede_multiplicar": True
})

print("Red energética inicial poblada con célula germinadora funcional.")
