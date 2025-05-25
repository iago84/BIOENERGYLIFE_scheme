from db import (
    generadores_table, config_table, celulas_table, organulos_table, tejidos_table,
    organos_table, tipos_table
)
import uuid


# 1. Limpiar todas las tablas
generadores_table.truncate()
config_table.truncate()
celulas_table.truncate()
organulos_table.truncate()
tejidos_table.truncate()
organos_table.truncate()
tipos_table.truncate()

# 2. Poblar tabla de TIPOS y FAMILIAS
familias_celulas = [
    {"codigo": "G", "nombre": "Germinadora"},
    {"codigo": "A", "nombre": "Amplificadora"},
    {"codigo": "S", "nombre": "Estabilizadora"},
    {"codigo": "D", "nombre": "Distribuidora"},
    {"codigo": "Z", "nombre": "Latente"},
    {"codigo": "C", "nombre": "Comunicadora"},
    {"codigo": "CGX", "nombre": "Germinadora Extendida"},
    {"codigo": "CEA", "nombre": "Amplificadora Evolutiva"},
    {"codigo": "CST", "nombre": "Transmisora Sináptica"},
    {"codigo": "CFB", "nombre": "Fusión Binaria"},
    {"codigo": "CVP", "nombre": "Progenitora Variable"}
]
tipos_organos = [
    {"codigo": "CP", "nombre": "Central Primario"},
    {"codigo": "CD", "nombre": "Central Distribuidor"},
    {"codigo": "CRE", "nombre": "Central Regulador Evolutivo"},
    {"codigo": "ODE", "nombre": "Órgano de Enlace"},
    {"codigo": "ODE+", "nombre": "Órgano de Enlace Plus"}
]
for familia in familias_celulas:
    tipos_table.insert({"clase": "celula", **familia})
for organo in tipos_organos:
    tipos_table.insert({"clase": "organo", **organo})

# 3. Poblar generadores avanzados (con métodos de arranque)
generadores = [
    {
        "id": "G-M100",
        "nombre": "Micro Generador Manual",
        "tipo": "iman_fijo",
        "potencia_kw": 0.1,
        "rpm_min": 60,
        "voltaje_salida_v": 12,
        "eficiencia": 0.75,
        "aplicacion": "O1",
        "arranques": [
            {"tipo": "manual", "descripcion": "Manivela o pedal", "costo_kw": 0.05}
        ],
        "notas": "Ideal para pruebas rápidas o backup local."
    },
    {
        "id": "G-I1K",
        "nombre": "Generador Inducción 1kW",
        "tipo": "induccion",
        "potencia_kw": 1.0,
        "rpm_min": 250,
        "voltaje_salida_v": 48,
        "eficiencia": 0.88,
        "aplicacion": "O3",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Impulso con motor 220V", "costo_kw": 0.2}
        ],
        "notas": "Requiere arranque externo inicial."
    },
    {
        "id": "G-I5K",
        "nombre": "Generador Inducción 5kW",
        "tipo": "induccion",
        "potencia_kw": 5.0,
        "rpm_min": 500,
        "voltaje_salida_v": 220,
        "eficiencia": 0.91,
        "aplicacion": "O4",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Arranque motor o red", "costo_kw": 1.0}
        ],
        "notas": "Potencia industrial. Arranque costoso."
    },
    {
        "id": "G-S500",
        "nombre": "Generador Solar 0.5kW",
        "tipo": "solar",
        "potencia_kw": 0.5,
        "rpm_min": 0,
        "voltaje_salida_v": 24,
        "eficiencia": 0.8,
        "aplicacion": "O1",
        "arranques": [
            {"tipo": "luz_solar", "descripcion": "Irradiancia mínima 300W/m2", "costo_kw": 0}
        ],
        "notas": "No requiere arranque, energía directa con luz solar."
    },
    {
        "id": "G-H2K",
        "nombre": "Generador Hidráulico 2kW",
        "tipo": "hidraulico",
        "potencia_kw": 2.0,
        "rpm_min": 300,
        "voltaje_salida_v": 120,
        "eficiencia": 0.92,
        "aplicacion": "O2",
        "arranques": [
            {"tipo": "flujo_agua", "descripcion": "Impulso hidráulico continuo", "costo_kw": 0.2}
        ],
        "notas": "Requiere caudal de agua estable."
    },
    # Puedes añadir más aquí según crezca tu catálogo
]
generadores_nuevos = [
    # Imán fijo: gama básica
    {
        "id": "G-M50",
        "nombre": "Micro Generador Manual Compacto",
        "tipo": "iman_fijo",
        "potencia_kw": 0.05,
        "rpm_min": 50,
        "voltaje_salida_v": 6,
        "eficiencia": 0.65,
        "aplicacion": "O1",
        "arranques": [
            {"tipo": "manual", "descripcion": "Manivela directa", "costo_kw": 0.02}
        ],
        "notas": "Baja potencia para emergencias o sensores."
    },
    {
        "id": "G-M200",
        "nombre": "Generador Manual Alta Resistencia",
        "tipo": "iman_fijo",
        "potencia_kw": 0.2,
        "rpm_min": 70,
        "voltaje_salida_v": 24,
        "eficiencia": 0.72,
        "aplicacion": "O2",
        "arranques": [
            {"tipo": "manual", "descripcion": "Palanca reforzada", "costo_kw": 0.08}
        ],
        "notas": "Utilizado en kits portátiles de emergencia."
    },
    {
        "id": "G-F1K",
        "nombre": "Generador Imán Fijo 1kW",
        "tipo": "iman_fijo",
        "potencia_kw": 1.0,
        "rpm_min": 150,
        "voltaje_salida_v": 48,
        "eficiencia": 0.83,
        "aplicacion": "O2",
        "arranques": [
            {"tipo": "manual", "descripcion": "Pedal motorizado inicial", "costo_kw": 0.15},
            {"tipo": "motor_aux", "descripcion": "Motor DC 12V", "costo_kw": 0.05}
        ],
        "notas": "Ideal para backups rurales y arranque híbrido."
    },
    {
        "id": "G-F2K",
        "nombre": "Generador Imán Fijo 2kW",
        "tipo": "iman_fijo",
        "potencia_kw": 2.0,
        "rpm_min": 200,
        "voltaje_salida_v": 110,
        "eficiencia": 0.85,
        "aplicacion": "O3",
        "arranques": [
            {"tipo": "manual", "descripcion": "Manivela larga", "costo_kw": 0.25},
            {"tipo": "corriente_externa", "descripcion": "Impulso inicial 220V", "costo_kw": 0.10}
        ],
        "notas": "Para pequeños talleres o núcleos familiares."
    },
    {
        "id": "G-F5K",
        "nombre": "Generador Imán Fijo 5kW",
        "tipo": "iman_fijo",
        "potencia_kw": 5.0,
        "rpm_min": 350,
        "voltaje_salida_v": 220,
        "eficiencia": 0.88,
        "aplicacion": "O3",
        "arranques": [
            {"tipo": "motor_aux", "descripcion": "Motor AC 220V", "costo_kw": 0.5}
        ],
        "notas": "Capacidad industrial básica, autoexcitable."
    },
    # Imán fijo: gama especial
    {
        "id": "G-F10K",
        "nombre": "Generador Imán Fijo 10kW Trifásico",
        "tipo": "iman_fijo",
        "potencia_kw": 10.0,
        "rpm_min": 400,
        "voltaje_salida_v": 400,
        "eficiencia": 0.92,
        "aplicacion": "O4",
        "arranques": [
            {"tipo": "motor_aux", "descripcion": "Motor trifásico externo", "costo_kw": 1.5}
        ],
        "notas": "Para racks modulares, alta estabilidad."
    },
    {
        "id": "G-F25K",
        "nombre": "Super Generador Imán Fijo 25kW",
        "tipo": "iman_fijo",
        "potencia_kw": 25.0,
        "rpm_min": 600,
        "voltaje_salida_v": 690,
        "eficiencia": 0.94,
        "aplicacion": "O5",
        "arranques": [
            {"tipo": "motor_aux", "descripcion": "Impulso de generador paralelo", "costo_kw": 2.5}
        ],
        "notas": "Para conexiones industriales de alto rendimiento."
    },
    # Inducción trifásica
    {
        "id": "G-T1K",
        "nombre": "Generador Trifásico Inducción 1kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 1.0,
        "rpm_min": 180,
        "voltaje_salida_v": 48,
        "eficiencia": 0.80,
        "aplicacion": "O2",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Impulso motor monofásico", "costo_kw": 0.25}
        ],
        "notas": "Ideal para pruebas y pequeños motores trifásicos."
    },
    {
        "id": "G-T2K",
        "nombre": "Generador Trifásico Inducción 2kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 2.0,
        "rpm_min": 200,
        "voltaje_salida_v": 110,
        "eficiencia": 0.82,
        "aplicacion": "O2",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Impulso motor AC 220V", "costo_kw": 0.35}
        ],
        "notas": "Rack modular, alimentación de bombas o maquinaria."
    },
    {
        "id": "G-T5K",
        "nombre": "Generador Trifásico Inducción 5kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 5.0,
        "rpm_min": 350,
        "voltaje_salida_v": 220,
        "eficiencia": 0.87,
        "aplicacion": "O3",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Motor trifásico o estrella-delta", "costo_kw": 0.7}
        ],
        "notas": "Rack industrial pequeño, talleres, backup crítico."
    },
    {
        "id": "G-T10K",
        "nombre": "Generador Trifásico Inducción 10kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 10.0,
        "rpm_min": 450,
        "voltaje_salida_v": 400,
        "eficiencia": 0.90,
        "aplicacion": "O4",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Arranque directo o soft-starter", "costo_kw": 1.2}
        ],
        "notas": "Para paneles de control, racks de mediana escala."
    },
    {
        "id": "G-T25K",
        "nombre": "Generador Trifásico Inducción 25kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 25.0,
        "rpm_min": 650,
        "voltaje_salida_v": 690,
        "eficiencia": 0.93,
        "aplicacion": "O5",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Arranque con variador de frecuencia", "costo_kw": 3.0}
        ],
        "notas": "Grandes sistemas, nodos de interconexión masiva."
    },
    # Otros ejemplos de especialidad (expande según lo que vayas necesitando)
    {
        "id": "G-T50K",
        "nombre": "Generador Trifásico Inducción 50kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 50.0,
        "rpm_min": 900,
        "voltaje_salida_v": 1000,
        "eficiencia": 0.95,
        "aplicacion": "O6",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Arranque programado en red", "costo_kw": 6.0}
        ],
        "notas": "Mega racks, plantas industriales, redes distribuidas."
    },
    # Puedes seguir añadiendo e iterando según necesidades...
]
generadores_industriales = [
    {
        "id": "G-T100K",
        "nombre": "Generador Trifásico Inducción 100kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 100.0,
        "rpm_min": 1000,
        "voltaje_salida_v": 1000,
        "eficiencia": 0.96,
        "aplicacion": "O7",
        "arranques": [
            {"tipo": "corriente_externa", "descripcion": "Variador de frecuencia industrial", "costo_kw": 12.0}
        ],
        "notas": "Industria pesada, backup hospitalario, mega-racks."
    },
    {
        "id": "G-T250K",
        "nombre": "Generador Trifásico Inducción 250kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 250.0,
        "rpm_min": 1200,
        "voltaje_salida_v": 3000,
        "eficiencia": 0.97,
        "aplicacion": "O7",
        "arranques": [
            {"tipo": "soft_starter", "descripcion": "Soft-Starter industrial PLC", "costo_kw": 25.0}
        ],
        "notas": "Grandes industrias, suministros críticos, aeropuertos."
    },
    {
        "id": "G-T500K",
        "nombre": "Generador Trifásico Inducción 500kW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 500.0,
        "rpm_min": 1400,
        "voltaje_salida_v": 6600,
        "eficiencia": 0.98,
        "aplicacion": "O8",
        "arranques": [
            {"tipo": "arranque_secundario", "descripcion": "Arranque en dos etapas, sincronizado", "costo_kw": 45.0}
        ],
        "notas": "Sistemas de cogeneración, plantas industriales mayores."
    },
    {
        "id": "G-T1MW",
        "nombre": "Generador Trifásico Inducción 1MW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 1000.0,
        "rpm_min": 1500,
        "voltaje_salida_v": 11000,
        "eficiencia": 0.985,
        "aplicacion": "O9",
        "arranques": [
            {"tipo": "sistema_sincronizado", "descripcion": "Sincronización de red, arranque programado", "costo_kw": 90.0}
        ],
        "notas": "Redes eléctricas, subestaciones, emergencias urbanas."
    },
    {
        "id": "G-T2MW",
        "nombre": "Generador Trifásico Inducción 2MW",
        "tipo": "induccion_trifasico",
        "potencia_kw": 2000.0,
        "rpm_min": 1500,
        "voltaje_salida_v": 15000,
        "eficiencia": 0.988,
        "aplicacion": "O10",
        "arranques": [
            {"tipo": "sistema_sincronizado", "descripcion": "Automatizado con redundancia", "costo_kw": 180.0}
        ],
        "notas": "Mega plantas, centrales distribuidas, grandes industrias."
    },
    {
        "id": "G-F500K",
        "nombre": "Generador Imán Fijo 500kW",
        "tipo": "iman_fijo",
        "potencia_kw": 500.0,
        "rpm_min": 1200,
        "voltaje_salida_v": 11000,
        "eficiencia": 0.985,
        "aplicacion": "O8",
        "arranques": [
            {"tipo": "motor_aux", "descripcion": "Arranque asistido con generador auxiliar", "costo_kw": 50.0}
        ],
        "notas": "Para industrias verdes y generación renovable en granja."
    },
    {
        "id": "G-F1MW",
        "nombre": "Super Generador Imán Fijo 1MW",
        "tipo": "iman_fijo",
        "potencia_kw": 1000.0,
        "rpm_min": 1200,
        "voltaje_salida_v": 15000,
        "eficiencia": 0.99,
        "aplicacion": "O10",
        "arranques": [
            {"tipo": "arranque_automatizado", "descripcion": "Secuencia automática de alta potencia", "costo_kw": 120.0}
        ],
        "notas": "Para interconexión de parques energéticos renovables."
    },
    {
        "id": "G-F2MW",
        "nombre": "Ultra Generador Imán Fijo 2MW",
        "tipo": "iman_fijo",
        "potencia_kw": 2000.0,
        "rpm_min": 1500,
        "voltaje_salida_v": 20000,
        "eficiencia": 0.992,
        "aplicacion": "O11",
        "arranques": [
            {"tipo": "arranque_dual", "descripcion": "Dual start: doble generador de arranque", "costo_kw": 210.0}
        ],
        "notas": "Para futuras ciudades inteligentes, hubs industriales."
    }
]

generadores.extend(generadores_nuevos)
generadores.extend(generadores_industriales)
generadores_table.insert_multiple(generadores)


# 4. Configuración general básica
config_table.insert_multiple([
    {"clave": "velocidad_simulacion", "valor": 1.0},
    {"clave": "energia_inicial", "valor": 10},
    {"clave": "ciclos_maximos", "valor": 1000}
])

# 5. POBLAR ORGÁNULOS Y CÉLULAS DE EJEMPLO (Técnica y germinadora)
def generar_organulos_cascada(
        celula_id="C1",
        n_secundarios=10,
        n_intermedios=5,
        potencia_sec=0.1,
        potencia_int=1.0,
        potencia_final=5.0
    ):
    organulos = []
    # Orgánulo maestro
    organulos.append({
        "id": f"O1-0",
        "tipo": "O1",
        "potencia": potencia_sec,
        "estado": "operativo",
        "celula_asociada": celula_id,
        "activa_a": [f"O1-{i}" for i in range(1, n_secundarios + 1)],
        "depende_de": [],
        "secuenciador": True
    })
    # Orgánulos secundarios
    for i in range(1, n_secundarios + 1):
        organulos.append({
            "id": f"O1-{i}",
            "tipo": "O1",
            "potencia": potencia_sec,
            "estado": "espera",
            "celula_asociada": celula_id,
            "activa_a": [],
            "depende_de": [f"O1-0"],
            "secuenciador": False
        })
    # Orgánulos intermedios conectados a secundarios (pares)
    for i in range(1, n_intermedios + 1):
        sec1 = (i * 2) - 1
        sec2 = i * 2
        organulos.append({
            "id": f"O3-{i}",
            "tipo": "O3",
            "potencia": potencia_int,
            "estado": "espera",
            "celula_asociada": celula_id,
            "activa_a": [f"O4-1"],
            "depende_de": [f"O1-{sec1}", f"O1-{sec2}"],
            "secuenciador": False
        })
    # Orgánulo final
    organulos.append({
        "id": f"O4-1",
        "tipo": "O4",
        "potencia": potencia_final,
        "estado": "espera",
        "celula_asociada": celula_id,
        "activa_a": [],
        "depende_de": [f"O3-{i}" for i in range(1, n_intermedios + 1)],
        "secuenciador": False
    })
    return organulos

organulos = generar_organulos_cascada("C1", n_secundarios=10, n_intermedios=5)
organulos_table.insert_multiple(organulos)

# 7. Poblar CELULAS tipo (plantillas avanzadas)
plantilla_germinadora = {
    "id": "C-G",
    "tipo": "G",
    "energia": 2.0,
    "organulos": [
        {"id": "O1-G-0", "tipo": "O1", "potencia": 0.2, "estado": "operativo"},
        {"id": "O11-G-1", "tipo": "O11", "potencia": 0.2, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": True,
    "consumo_kw": 0.1,
    "produccion_kw": 0.2,
    "energia_maxima": 5.0,
    "historial": ["Célula germinadora creada y autoactivada."]
}

plantilla_amplificadora = {
    "id": "C-A",
    "tipo": "A",
    "energia": 1.5,
    "organulos": [
        {"id": "O3-A-1", "tipo": "O3", "potencia": 0.5, "estado": "operativo"},
        {"id": "O1-A-1", "tipo": "O1", "potencia": 0.1, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": True,
    "consumo_kw": 0.15,
    "produccion_kw": 0.5,
    "energia_maxima": 3.0,
    "historial": ["Célula amplificadora lista, orgánulo O3 encendido."]
}

plantilla_estabilizadora = {
    "id": "C-S",
    "tipo": "S",
    "energia": 0.4,
    "organulos": [
        {"id": "O2-S-1", "tipo": "O2", "potencia": 0.05, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": False,
    "consumo_kw": 0.05,
    "produccion_kw": 0.0,
    "energia_maxima": 1.0,
    "historial": ["Estabilizadora activa, equilibrando voltajes."]
}

plantilla_distribuidora = {
    "id": "C-D",
    "tipo": "D",
    "energia": 0.6,
    "organulos": [
        {"id": "O5-D-1", "tipo": "O5", "potencia": 0.1, "estado": "operativo"},
        {"id": "O1-D-1", "tipo": "O1", "potencia": 0.05, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": False,
    "consumo_kw": 0.08,
    "produccion_kw": 0.0,
    "energia_maxima": 2.0,
    "historial": ["Distribuidora lista para dividir energía."]
}

plantilla_latente = {
    "id": "C-Z",
    "tipo": "Z",
    "energia": 0.1,
    "organulos": [
        {"id": "O8-Z-1", "tipo": "O8", "potencia": 0.05, "estado": "en_reserva"}
    ],
    "estado": "latente",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": False,
    "consumo_kw": 0.01,
    "produccion_kw": 0.05,
    "energia_maxima": 0.5,
    "historial": ["Latente: espera activación de emergencia."]
}

plantilla_comunicadora = {
    "id": "C-C",
    "tipo": "C",
    "energia": 0.2,
    "organulos": [
        {"id": "O7-C-1", "tipo": "O7", "potencia": 0.02, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": False,
    "consumo_kw": 0.02,
    "produccion_kw": 0.0,
    "energia_maxima": 1.0,
    "historial": ["Comunicadora conectada a la red."]
}

plantilla_germinadora_extendida = {
    "id": "C-CGX",
    "tipo": "CGX",
    "energia": 2.2,
    "organulos": [
        {"id": "O1-CGX-0", "tipo": "O1", "potencia": 0.2, "estado": "operativo"},
        {"id": "O11-CGX-1", "tipo": "O11", "potencia": 0.4, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": True,
    "consumo_kw": 0.08,
    "produccion_kw": 0.3,
    "energia_maxima": 6.0,
    "historial": ["Célula germinadora extendida auto-regenerativa."]
}

plantilla_amplificadora_evolutiva = {
    "id": "C-CEA",
    "tipo": "CEA",
    "energia": 1.7,
    "organulos": [
        {"id": "O3-CEA-1", "tipo": "O3", "potencia": 0.7, "estado": "operativo"},
        {"id": "O2-CEA-1", "tipo": "O2", "potencia": 0.2, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": True,
    "consumo_kw": 0.12,
    "produccion_kw": 0.7,
    "energia_maxima": 3.5,
    "historial": ["Célula amplificadora evolutiva lista."]
}

plantilla_transmisora_sinaptica = {
    "id": "C-CST",
    "tipo": "CST",
    "energia": 0.3,
    "organulos": [
        {"id": "O9-CST-1", "tipo": "O9", "potencia": 0.03, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": False,
    "consumo_kw": 0.04,
    "produccion_kw": 0.0,
    "energia_maxima": 0.8,
    "historial": ["Transmisora sináptica conectada."]
}

plantilla_fusion_binaria = {
    "id": "C-CFB",
    "tipo": "CFB",
    "energia": 0.8,
    "organulos": [
        {"id": "O6-CFB-1", "tipo": "O6", "potencia": 0.4, "estado": "operativo"},
        {"id": "O6-CFB-2", "tipo": "O6", "potencia": 0.3, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": True,
    "consumo_kw": 0.1,
    "produccion_kw": 0.4,
    "energia_maxima": 2.0,
    "historial": ["Célula de fusión preparada para integrar energía."]
}

plantilla_progenitora_variable = {
    "id": "C-CVP",
    "tipo": "CVP",
    "energia": 0.7,
    "organulos": [
        {"id": "O10-CVP-1", "tipo": "O10", "potencia": 0.15, "estado": "operativo"}
    ],
    "estado": "activa",
    "generacion": 1,
    "atributos": {},
    "estable": True,
    "productiva": True,
    "consumo_kw": 0.05,
    "produccion_kw": 0.15,
    "energia_maxima": 1.5,
    "historial": ["Progenitora variable: lista para adaptarse."]
}

todas_plantillas = [
    plantilla_germinadora,
    plantilla_amplificadora,
    plantilla_estabilizadora,
    plantilla_distribuidora,
    plantilla_latente,
    plantilla_comunicadora,
    plantilla_germinadora_extendida,
    plantilla_amplificadora_evolutiva,
    plantilla_transmisora_sinaptica,
    plantilla_fusion_binaria,
    plantilla_progenitora_variable
]
# Diccionario automático (clave = tipo):
dict_plantillas = {p["tipo"]: p for p in todas_plantillas}

for celula in todas_plantillas:
    celulas_table.insert(celula)


def crear_celula_instancia(id, tipo, energia, organulos, ubicacion, madre=None, estado="activa", nivel_evolucion=1, enlaces=None, puede_multiplicar=True, posibles_evoluciones=None):
    celulas_table.insert({
        "id": id,
        "tipo": tipo,
        "energia_actual": energia,
        "energia_maxima": 10,
        "organulos": organulos,
        "estado": estado,
        "ubicacion": ubicacion,
        "nivel_evolucion": nivel_evolucion,
        "enlaces": enlaces or [],
        "generada_por": madre,
        "puede_multiplicar": puede_multiplicar,
        "posibles_evoluciones": posibles_evoluciones or []
    })



def instanciar_celula_desde_plantilla(
    plantilla,
    posicion,             # Dict: {"x": int, "y": int}
    madre=None,
    sufijo_id=None,
    estado="activa",
    nivel_evolucion=1,
    enlaces=None,
    puede_multiplicar=True,
    posibles_evoluciones=None
):
    # Crea ID único si no se especifica sufijo
    celula_id = plantilla["id"] + ("_" + sufijo_id if sufijo_id else "_" + str(uuid.uuid4())[:8])
    # Clona organulos cambiando IDs
    organulos = []
    organulo_ids = []
    for o in plantilla["organulos"]:
        oid = f"{celula_id}-{o['id']}"
        organulos.append({**o, "id": oid, "celula_asociada": celula_id})
        organulo_ids.append(oid)
    organulos_table.insert_multiple(organulos)
    # Inserta célula
    celulas_table.insert({
        "id": celula_id,
        "tipo": plantilla["tipo"],
        "energia_actual": plantilla.get("energia", 0),
        "energia_maxima": plantilla.get("energia_maxima", 10),
        "organulos": organulo_ids,
        "estado": estado,
        "ubicacion": posicion,
        "nivel_evolucion": nivel_evolucion,
        "enlaces": enlaces or [],
        "generada_por": madre,
        "puede_multiplicar": puede_multiplicar,
        "posibles_evoluciones": posibles_evoluciones or [],
        "estable": plantilla.get("estable"),
        "productiva": plantilla.get("productiva"),
        "consumo_kw": plantilla.get("consumo_kw"),
        "produccion_kw": plantilla.get("produccion_kw"),
        "historial": plantilla.get("historial", []),
        "atributos": plantilla.get("atributos", {}),
        "generacion": plantilla.get("generacion", 1)
    })
    return celula_id, organulo_ids


def poblar_celulas_canvas():
    posiciones = [
        {"x": 100, "y": 100},
        {"x": 300, "y": 100},
        {"x": 500, "y": 300},
        {"x": 700, "y": 100}
    ]
    plantillas = [
        plantilla_germinadora,
        plantilla_amplificadora,
        plantilla_estabilizadora,
        plantilla_distribuidora
    ]
    celulas_info = []
    for i, plantilla in enumerate(plantillas):
        celula_id, organulo_ids = instanciar_celula_desde_plantilla(
            plantilla=plantilla,
            posicion=posiciones[i],
            madre=None,
            sufijo_id=str(i+1)
        )
        celulas_info.append({
            "id": celula_id,
            "tipo": plantilla["tipo"],
            "x": posiciones[i]["x"],
            "y": posiciones[i]["y"],
            "organulos": organulo_ids
        })
    return celulas_info  # -> lo mandas directo al frontend/canvas para pintar


