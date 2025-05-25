import sqlite3
import json
import os

# Ruta al archivo JSON de TinyDB (ajústala si es necesario)
db_json_path = "backend/db_simulador.json"
sqlite_path = "simulador.db"

# Carga los datos del JSON
with open(db_json_path, 'r', encoding='utf-8') as f:
    db_data = json.load(f)

conn = sqlite3.connect(sqlite_path)
cur = conn.cursor()

def crear_tabla(nombre, primer_registro):
    campos = []
    for k, v in primer_registro.items():
        tipo = "TEXT"
        if isinstance(v, int):
            tipo = "INTEGER"
        elif isinstance(v, float):
            tipo = "REAL"
        elif isinstance(v, dict) or isinstance(v, list):
            tipo = "TEXT"
        campos.append(f'"{k}" {tipo}')
    campos_sql = ", ".join(campos)
    cur.execute(f'DROP TABLE IF EXISTS "{nombre}"')
    cur.execute(f'CREATE TABLE "{nombre}" ({campos_sql})')

def insertar_registros(nombre, registros):
    if not registros:
        return
    keys = list(registros[0].keys())
    qmarks = ", ".join(["?"] * len(keys))
    for reg in registros:
        vals = []
        for k in keys:
            v = reg.get(k, None)
            if isinstance(v, dict) or isinstance(v, list):
                v = json.dumps(v)
            vals.append(v)
        cur.execute(f'INSERT INTO "{nombre}" ({", ".join(keys)}) VALUES ({qmarks})', vals)

for tabla, data in db_data.get('_default', {}).items():
    print(f"Procesando tabla: {tabla} ({len(data)} registros)")
    if not data:
        continue
    crear_tabla(tabla, data[0])
    insertar_registros(tabla, data)

conn.commit()
conn.close()
print(f"¡Conversión completada! Base de datos SQLite creada en: {sqlite_path}")
