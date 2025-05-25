from db import logs_table
from collections import Counter
from datetime import datetime

def resumen_logs():
    logs = logs_table.all()
    resumen = {
        "total_eventos": len(logs),
        "tipos_eventos": Counter(log["tipo"] for log in logs),
        "ultimos_eventos": sorted(logs, key=lambda x: x["timestamp"], reverse=True)[:10]
    }

    print("\n=== RESUMEN DE LOGS ===")
    print(f"Total eventos registrados: {resumen['total_eventos']}")
    print("Eventos por tipo:")
    for tipo, count in resumen['tipos_eventos'].items():
        print(f"  - {tipo}: {count}")
    print("\nÚltimos 10 eventos:")
    for ev in resumen["ultimos_eventos"]:
        timestamp = datetime.fromisoformat(ev["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ({ev['tipo']}) {ev['descripcion']}")

if __name__ == "__main__":
    resumen_logs()
