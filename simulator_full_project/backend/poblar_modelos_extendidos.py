from db import generadores_table, organos_table, tejidos_table

def poblar_generadores_avanzados():
    generadores_table.insert_multiple([
        {"id": "G-NV800", "nombre": "Generador Nanovoltaje", "tipo": "nanovoltaje", "potencia_kw": 0.01, "rpm_min": 30, "voltaje_salida_v": 1, "eficiencia": 0.65, "aplicacion": "O7, sensores"},
        {"id": "G-SOL20", "nombre": "Panel Solar 20W", "tipo": "solar", "potencia_kw": 0.02, "rpm_min": 0, "voltaje_salida_v": 12, "eficiencia": 0.80, "aplicacion": "O8, mantenimiento"},
        {"id": "G-TR10K", "nombre": "Turbina 10kW", "tipo": "turbina", "potencia_kw": 10.0, "rpm_min": 1200, "voltaje_salida_v": 400, "eficiencia": 0.92, "aplicacion": "CP soporte"},
        {"id": "G-MOD2X", "nombre": "Generador Modular Dual", "tipo": "modular", "potencia_kw": 2.0, "rpm_min": 800, "voltaje_salida_v": 220, "eficiencia": 0.90, "aplicacion": "backup redundante"},
        {"id": "G-PSYNC50", "nombre": "Sincrónico Puro 50kW", "tipo": "sincrono", "potencia_kw": 50.0, "rpm_min": 1800, "voltaje_salida_v": 380, "eficiencia": 0.95, "aplicacion": "CD sincronizado"}
    ])

def poblar_organos_avanzados():
    organos_table.insert_multiple([
        {"id": "ODE1", "tipo": "ODE", "energia_in": 2.0, "energia_out": 1.9, "estado": "activo", "asociados": ["CP1"]},
        {"id": "ODEPLUS", "tipo": "ODE+", "energia_in": 5.0, "energia_out": 4.9, "estado": "activo", "asociados": ["T4", "CD1"]}
    ])

def poblar_tejidos_avanzados():
    tejidos_table.insert_multiple([
        {"id": "T4", "tipo": "T4", "celulas": ["C1", "C2"], "funcion": "contingencia", "nodo_destino": "CRE1"},
        {"id": "T5", "tipo": "T5", "celulas": ["C3", "C4", "C5", "C6"], "funcion": "propagacion_hex", "nodo_destino": "CP2"},
        {"id": "T6", "tipo": "T6", "celulas": ["C7", "C8", "C9"], "funcion": "regulacion_global", "nodo_destino": "ODEPLUS"}
    ])

def poblar_modelos_extendidos():
    poblar_generadores_avanzados()
    poblar_organos_avanzados()
    poblar_tejidos_avanzados()
    print("Modelos extendidos poblados con éxito.")

if __name__ == "__main__":
    poblar_modelos_extendidos()
