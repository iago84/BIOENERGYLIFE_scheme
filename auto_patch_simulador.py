import os
import re

# ========================
# CONFIGURACIÓN
# ========================

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
BACKEND_FILES = [
    'server.py', 'controller.py', 'db.py', 'populate_db.py',
    'engine.py', 'logger.py', 'costs_and_requirements.py'
]
FRONTEND_FILES = [
    os.path.join('frontend', 'index.html'),
    os.path.join('frontend', 'app.js'),
    os.path.join('frontend', 'style.css')
]
LOG = []
CORRECCIONES_REALIZADAS = []

def leer_archivo(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def escribir_archivo(path, texto):
    with open(path, "w", encoding="utf-8") as f:
        f.write(texto)

def check_lineas_codigo(texto, patrones):
    return [bool(re.search(p, texto)) for p in patrones]

# ==================================
# PARCHES POR ARCHIVO
# ==================================

def parchear_server(path):
    texto = leer_archivo(path)
    acciones = []
    # --- Endpoints faltantes ---
    endpoints = {
        "/api/conectar": "def api_conectar():",
        "/api/desconectar": "def api_desconectar():",
        "/api/random_param": "def api_random_param():",
        "/api/random": "def api_random():"
    }
    for endpoint, fn in endpoints.items():
        if endpoint not in texto:
            acciones.append(f"[+] Añadiendo endpoint: {endpoint}")
            if endpoint == "/api/desconectar":
                patch = """
@app.route("/api/desconectar", methods=["POST"])
def api_desconectar():
    data = request.json
    from controller import desconectar_celulas
    desconectar_celulas(data["origen"], data["destino"])
    return jsonify({"ok": True})
"""
            elif endpoint == "/api/random_param":
                patch = """
@app.route("/api/random_param", methods=["POST"])
def api_random_param():
    data = request.json
    from controller import randomizar_organismo_param
    resultado = randomizar_organismo_param(data)
    return jsonify({"ok": True, "resultado": resultado})
"""
            elif endpoint == "/api/random":
                patch = """
@app.route("/api/random", methods=["POST"])
def api_random():
    from controller import randomizar_organismo
    resultado = randomizar_organismo()
    return jsonify({"ok": True, "resultado": resultado})
"""
            else:
                patch = ""
            texto += "\n" + patch
    # --- Final ---
    if acciones:
        escribir_archivo(path, texto)
    return acciones

def parchear_controller(path):
    texto = leer_archivo(path)
    acciones = []
    # --- Funciones faltantes ---
    faltantes = {
        "def instanciar_celula_tipo": """
def instanciar_celula_tipo(tipo, posicion, madre=None):
    from populate_db import todas_plantillas, instanciar_celula_desde_plantilla
    plantilla = next((p for p in todas_plantillas if p["tipo"] == tipo), None)
    if not plantilla:
        raise ValueError(f"Tipo de célula desconocido: {tipo}")
    nueva_id, _ = instanciar_celula_desde_plantilla(
        plantilla=plantilla,
        posicion=posicion,
        madre=madre,
        sufijo_id=None,
        estado="activa",
        nivel_evolucion=1,
        enlaces=[],
        posibles_evoluciones=plantilla.get("posibles_evoluciones", [])
    )
    return nueva_id
""",
        "def editar_celula": """
def editar_celula(celula_id, cambios: dict):
    from db import celulas_table
    celulas_table.update(cambios, lambda c: c["id"] == celula_id)
""",
        "def eliminar_celula": """
def eliminar_celula(celula_id):
    from db import celulas_table, organulos_table
    celulas_table.delete(lambda c: c["id"] == celula_id)
    organulos_table.delete(lambda o: o["celula_asociada"] == celula_id)
""",
        "def conectar_celulas": """
def conectar_celulas(origen, destino):
    from db import celulas_table
    celulas_table.update(
        lambda c: c["id"] == origen,
        lambda c: c.setdefault("enlaces", []).append(destino)
    )
""",
        "def desconectar_celulas": """
def desconectar_celulas(origen, destino):
    from db import celulas_table
    celulas_table.update(
        lambda c: c["id"] == origen,
        lambda c: c["enlaces"].remove(destino) if destino in c["enlaces"] else None
    )
""",
        "def clonar_celula": """
def clonar_celula(celula_id, posicion):
    from db import celulas_table, organulos_table
    import copy, uuid
    cel = celulas_table.get(lambda c: c["id"] == celula_id)
    if not cel:
        return None
    nueva_id = celula_id + "-CLONE-" + uuid.uuid4().hex[:4]
    nuevos_organulos = []
    for oid in cel["organulos"]:
        org = organulos_table.get(lambda o: o["id"] == oid)
        if org:
            nuevo_org = copy.deepcopy(org)
            nuevo_org["id"] = nueva_id + "-" + org["id"]
            nuevo_org["celula_asociada"] = nueva_id
            nuevos_organulos.append(nuevo_org)
    organulos_table.insert_multiple(nuevos_organulos)
    nueva_cel = copy.deepcopy(cel)
    nueva_cel["id"] = nueva_id
    nueva_cel["ubicacion"] = posicion
    nueva_cel["organulos"] = [o["id"] for o in nuevos_organulos]
    celulas_table.insert(nueva_cel)
    return nueva_id
""",
        "def reiniciar_red": """
def reiniciar_red():
    from populate_db import poblar_celulas_canvas
    poblar_celulas_canvas()
""",
        "def randomizar_organismo": """
def randomizar_organismo():
    from populate_db import poblar_red_random
    return poblar_red_random()
""",
        "def randomizar_organismo_param": """
def randomizar_organismo_param(params):
    from populate_db import poblar_red_random_param
    return poblar_red_random_param(params)
""",
    }
    for fn, code in faltantes.items():
        if fn not in texto:
            acciones.append(f"[+] Añadiendo función: {fn}")
            texto += "\n" + code
    if acciones:
        escribir_archivo(path, texto)
    return acciones

def parchear_populate_db(path):
    texto = leer_archivo(path)
    acciones = []
    # --- Random total ---
    if "def poblar_red_random(" not in texto:
        acciones.append("[+] Añadiendo función poblar_red_random (random total)")
        code = """
def poblar_red_random():
    import random
    from db import celulas_table, organulos_table
    from populate_db import todas_plantillas, instanciar_celula_desde_plantilla
    celulas_table.truncate()
    organulos_table.truncate()
    posiciones = []
    for i in range(10):
        posiciones.append({"x": random.randint(80,1000), "y": random.randint(80,700)})
    for i, plantilla in enumerate(random.sample(todas_plantillas, 4)):
        instanciar_celula_desde_plantilla(
            plantilla=plantilla,
            posicion=posiciones[i],
            madre=None,
            sufijo_id=str(i+1),
            estado="activa",
            nivel_evolucion=1,
            enlaces=[],
            posibles_evoluciones=plantilla.get("posibles_evoluciones", [])
        )
    return "Organismo randomizado"
"""
        texto += "\n" + code
    # --- Random por parámetros ---
    if "def poblar_red_random_param(" not in texto:
        acciones.append("[+] Añadiendo función poblar_red_random_param (random por parámetros)")
        code = """
def poblar_red_random_param(params):
    import random
    from db import celulas_table, organulos_table
    from populate_db import todas_plantillas, instanciar_celula_desde_plantilla
    celulas_table.truncate()
    organulos_table.truncate()
    n = int(params.get("numCelulas", 10))
    tipos_pct = [
        ("G", int(params.get("pctGerminadoras", 30))),
        ("A", int(params.get("pctAmplificadoras", 20))),
        ("D", int(params.get("pctDistribuidoras", 20))),
        ("S", int(params.get("pctEstabilizadoras", 20))),
    ]
    tipos_list = []
    for tipo, pct in tipos_pct:
        count = int((pct/100)*n)
        tipos_list.extend([tipo]*count)
    while len(tipos_list) < n:
        tipos_list.append(random.choice(["G","A","D","S"]))
    random.shuffle(tipos_list)
    posiciones = [{"x": random.randint(80,1100), "y": random.randint(80,700)} for _ in range(n)]
    for i in range(n):
        plantilla = next((p for p in todas_plantillas if p["tipo"]==tipos_list[i]), todas_plantillas[0])
        instanciar_celula_desde_plantilla(
            plantilla=plantilla,
            posicion=posiciones[i],
            madre=None,
            sufijo_id=str(i+1),
            estado="activa",
            nivel_evolucion=1,
            enlaces=[],
            posibles_evoluciones=plantilla.get("posibles_evoluciones", [])
        )
    return f"{n} células randomizadas según parámetros"
"""
        texto += "\n" + code
    if acciones:
        escribir_archivo(path, texto)
    return acciones

def parchear_frontend_js(path):
    texto = leer_archivo(path)
    acciones = []
    # TODO: Podríamos inyectar aquí helpers para drag&drop, edición y fetch avanzado si falta.
    if "fetch(" not in texto:
        acciones.append("[!] Advertencia: fetch/ajax no encontrado. Asegúrate de tener comunicación con backend.")
    if "function crearCelulaManual" not in texto:
        acciones.append("[+] Sugerencia: Añadir función crearCelulaManual() y modal de edición/creación.")
    if acciones:
        print("[FRONTEND] app.js:", acciones)
    return acciones

def parchear_frontend_html(path):
    texto = leer_archivo(path)
    acciones = []
    # TODO: Sugerir punto de inserción de modales, paneles info, etc.
    if "<!-- MODAL EDICION -->" not in texto:
        acciones.append("[+] Añadir modal de edición manual (célula).")
    if acciones:
        print("[FRONTEND] index.html:", acciones)
    return acciones

import re

BLOQUES_CSS = {
    "modal": """
/* --- MODAL BÁSICO --- */
.modal {
  position: fixed; z-index: 999; left: 0; top: 0; width: 100vw; height: 100vh;
  display: flex; align-items: center; justify-content: center;
  background: rgba(0,0,0,0.4); transition: background 0.3s;
}
.modal-content {
  background: #fff; color: #222; padding: 2em 2em 1em 2em; border-radius: 16px; box-shadow: 0 6px 32px #0004;
  min-width: 300px; min-height: 160px; position: relative; max-width: 95vw; max-height: 80vh; overflow: auto;
}
.modal .close { position: absolute; top: 12px; right: 16px; font-size: 2em; cursor: pointer; }
    """,

    "dragging": """
/* --- DRAG & DROP --- */
.dragging { opacity: 0.7; box-shadow: 0 0 24px #1af, 0 0 0 2px #1af inset; }
    """,

    "darkmode": """
/* --- DARK MODE --- */
body.dark, body[data-theme="dark"] {
  background: #222 !important; color: #eee !important;
}
body.dark #sidebar { background: #111; }
body.dark .modal-content { background: #222; color: #eee; }
    """,

    "transition": """
/* --- TRANSICIONES SUAVES --- */
button, .modal, #sidebar, canvas, .celula, .selected {
  transition: all 0.25s cubic-bezier(.4,.22,.2,1.1);
}
    """,

    "sidebar": """
/* --- SIDEBAR MODERNO --- */
#sidebar {
  width: 320px; min-width: 200px; max-width: 400px; background: #fafafa;
  border-right: 2px solid #2222; box-shadow: 2px 0 16px #0002;
  padding: 24px 18px 12px 18px; height: 100vh; overflow-y: auto; position: fixed; left: 0; top: 0;
}
    """,

    "selected": """
/* --- SELECCIÓN DE CÉLULA --- */
.selected {
  outline: 3px solid #1af; outline-offset: 2px;
  background: linear-gradient(90deg, #e0f7fa 40%, #b2ebf2 100%);
}
    """,
}

def parchear_frontend_css(path):
    texto = leer_archivo(path)
    acciones = []
    # Revisar e inyectar bloques si faltan
    for clave, bloque in BLOQUES_CSS.items():
        pattern = r"\." + re.escape(clave)
        if clave == "sidebar":
            pattern = r"#sidebar"
        if clave == "darkmode":
            pattern = r"body\.dark|body\[data-theme=\"dark\"\]"
        if clave == "transition":
            pattern = r"transition"
        if clave == "selected":
            pattern = r"\.selected"
        if not re.search(pattern, texto):
            texto += "\n" + bloque + "\n"
            acciones.append(f"[APLICADO] Añadido bloque CSS para {clave}")
    if acciones:
        guardar_archivo(path, texto)
    return acciones

def guardar_archivo(path, texto):
    with open(path, "w", encoding="utf-8") as f:
        f.write(texto)

# ==========================
# MAIN CHECK & PATCHER
# ==========================


def main():
    print("==== AUTO-PATCH SIMULADOR ORGÁNICO ====")
    archivos = BACKEND_FILES + FRONTEND_FILES
    resumen = {}
    for file in archivos:
        p = os.path.join(PROJECT_ROOT, file)
        if not os.path.exists(p):
            LOG.append(f"[!] {file} no encontrado.")
            continue
        print(f"--- Revisando {file} ---")
        if file.endswith('server.py'):
            acciones = parchear_server(p)
        elif file.endswith('controller.py'):
            acciones = parchear_controller(p)
        elif file.endswith('populate_db.py'):
            acciones = parchear_populate_db(p)
        elif file.endswith('app.js'):
            acciones = parchear_frontend_js(p)
        elif file.endswith('index.html'):
            acciones = parchear_frontend_html(p)
        elif file.endswith('style.css'):
            acciones = parchear_frontend_css(p)
        else:
            acciones = []
        resumen[file] = acciones
        if acciones:
            CORRECCIONES_REALIZADAS.extend([f"{file}: {a}" for a in acciones])
    # Output resumen
    print("\n===== RESUMEN =====")
    for k,v in resumen.items():
        if v:
            print(f"{k}:")
            for a in v:
                print("   ", a)
    print("\n[INFO] Script completado.")
    print(f"Correcciones/añadidos: {len(CORRECCIONES_REALIZADAS)}")
    if CORRECCIONES_REALIZADAS:
        print("Detalles:")
        for l in CORRECCIONES_REALIZADAS:
            print("   ", l)
    print("\n[EXTRA] Revisa TODO los avisos manuales y adapta el frontend si tienes custom logic en JS/HTML/CSS.")
    print("[FIN] Puedes relanzar tu servidor. Si hay errores, mira los logs y vuelve a ejecutar este script.")

if __name__ == "__main__":
    main()



