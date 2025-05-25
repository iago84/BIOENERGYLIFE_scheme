from db import logs_table
from datetime import datetime

def log_event(tipo, descripcion, entidad_id=None):
    logs_table.insert({
        "timestamp": datetime.utcnow().isoformat(),
        "tipo": tipo,
        "descripcion": descripcion,
        "entidad_id": entidad_id
    })
    print(f"[LOG] ({tipo}) {descripcion} -> {entidad_id if entidad_id else ''}")
