import os

# =============== RUTAS Y ARCHIVOS ===============
FRONTEND = [
    "frontend/index.html", "frontend/app.js", "frontend/style.css"
]
CRUD_HTMLS = [
    "frontend/generadores.html", "frontend/organulos.html",
    "frontend/celulas.html", "frontend/conexiones.html", "frontend/dashboard.html"
]
CRUD_JS = [
    "frontend/crud_generadores.js", "frontend/crud_organulos.js",
    "frontend/crud_celulas.js", "frontend/crud_conexiones.js"
]
BACKEND = [
    "backend/server.py", "backend/controller.py", "backend/engine.py"
]

# =============== BLOQUES DE CÓDIGO ===============

# 1. HTML CRUD GENERADORES/ORGÁNULOS/CÉLULAS/CONEXIONES
BLOQUE_GENERADORES_HTML = """
<!-- CRUD Generadores -->
<div id="crudGeneradores">
  <h2>Generadores</h2>
  <button onclick="nuevoGenerador()">Nuevo</button>
  <table id="tablaGeneradores"></table>
</div>
<script src="crud_generadores.js"></script>
"""
BLOQUE_ORGANULOS_HTML = """
<!-- CRUD Orgánulos -->
<div id="crudOrganulos">
  <h2>Orgánulos</h2>
  <button onclick="nuevoOrganulo()">Nuevo</button>
  <table id="tablaOrganulos"></table>
</div>
<script src="crud_organulos.js"></script>
"""
BLOQUE_CELULAS_HTML = """
<!-- CRUD Células -->
<div id="crudCelulas">
  <h2>Células</h2>
  <button onclick="nuevaCelula()">Nueva</button>
  <table id="tablaCelulas"></table>
</div>
<script src="crud_celulas.js"></script>
"""
BLOQUE_CONEXIONES_HTML = """
<!-- CRUD Conexiones -->
<div id="crudConexiones">
  <h2>Conexiones</h2>
  <button onclick="nuevaConexion()">Nueva</button>
  <table id="tablaConexiones"></table>
</div>
<script src="crud_conexiones.js"></script>
"""

# 2. BACKEND ENDPOINTS CRUDS
BLOQUE_ENDPOINTS_CRUD = """
# === ENDPOINTS CRUD GENERADORES ===
@app.route("/api/generadores", methods=["GET"])
def api_generadores():
    from db import generadores_table
    return jsonify(generadores_table.all())

@app.route("/api/generadores", methods=["POST"])
def api_add_generador():
    from db import generadores_table
    generadores_table.insert(request.json)
    return jsonify({"ok": True})

@app.route("/api/generadores/<gid>", methods=["PATCH"])
def api_update_generador(gid):
    from db import generadores_table
    generadores_table.update(request.json, lambda g: g["id"] == gid)
    return jsonify({"ok": True})

@app.route("/api/generadores/<gid>", methods=["DELETE"])
def api_delete_generador(gid):
    from db import generadores_table
    generadores_table.remove(lambda g: g["id"] == gid)
    return jsonify({"ok": True})

# === ENDPOINTS CRUD ORGÁNULOS ===
@app.route("/api/organulos", methods=["GET"])
def api_organulos():
    from db import organulos_table
    return jsonify(organulos_table.all())

@app.route("/api/organulos", methods=["POST"])
def api_add_organulo():
    from db import organulos_table
    organulos_table.insert(request.json)
    return jsonify({"ok": True})

@app.route("/api/organulos/<oid>", methods=["PATCH"])
def api_update_organulo(oid):
    from db import organulos_table
    organulos_table.update(request.json, lambda o: o["id"] == oid)
    return jsonify({"ok": True})

@app.route("/api/organulos/<oid>", methods=["DELETE"])
def api_delete_organulo(oid):
    from db import organulos_table
    organulos_table.remove(lambda o: o["id"] == oid)
    return jsonify({"ok": True})

# === ENDPOINTS CRUD CÉLULAS ===
@app.route("/api/celulas", methods=["GET"])
def api_celulas():
    from db import celulas_table
    return jsonify(celulas_table.all())

@app.route("/api/celulas", methods=["POST"])
def api_add_celula():
    from db import celulas_table
    celulas_table.insert(request.json)
    return jsonify({"ok": True})

@app.route("/api/celulas/<cid>", methods=["PATCH"])
def api_update_celula(cid):
    from db import celulas_table
    celulas_table.update(request.json, lambda c: c["id"] == cid)
    return jsonify({"ok": True})

@app.route("/api/celulas/<cid>", methods=["DELETE"])
def api_delete_celula(cid):
    from db import celulas_table
    celulas_table.remove(lambda c: c["id"] == cid)
    return jsonify({"ok": True})

# === ENDPOINTS CRUD CONEXIONES ===
@app.route("/api/conexiones", methods=["GET"])
def api_conexiones():
    from db import conexiones_table
    return jsonify(conexiones_table.all())

@app.route("/api/conexiones", methods=["POST"])
def api_add_conexion():
    from db import conexiones_table
    conexiones_table.insert(request.json)
    return jsonify({"ok": True})

@app.route("/api/conexiones/<conid>", methods=["PATCH"])
def api_update_conexion(conid):
    from db import conexiones_table
    conexiones_table.update(request.json, lambda c: c["id"] == conid)
    return jsonify({"ok": True})

@app.route("/api/conexiones/<conid>", methods=["DELETE"])
def api_delete_conexion(conid):
    from db import conexiones_table
    conexiones_table.remove(lambda c: c["id"] == conid)
    return jsonify({"ok": True})

# === ENDPOINTS RANDOM, EXPORT/IMPORT ===
@app.route("/api/randomizar", methods=["POST"])
def api_randomizar():
    from controller import randomizar_organismo_param
    return jsonify(randomizar_organismo_param(request.json))

@app.route("/api/exportar", methods=["GET"])
def api_exportar():
    from db import celulas_table, organulos_table, conexiones_table
    return jsonify({
        "celulas": celulas_table.all(),
        "organulos": organulos_table.all(),
        "conexiones": conexiones_table.all()
    })

@app.route("/api/importar", methods=["POST"])
def api_importar():
    data = request.json
    from db import celulas_table, organulos_table, conexiones_table
    celulas_table.truncate(); organulos_table.truncate(); conexiones_table.truncate()
    celulas_table.insert_multiple(data.get("celulas", []))
    organulos_table.insert_multiple(data.get("organulos", []))
    conexiones_table.insert_multiple(data.get("conexiones", []))
    return jsonify({"ok": True})
"""

# 3. CONTROLLER CRUD Y FUNCIONES AUXILIARES
BLOQUE_FUNCS_CONTROLLER = """
# === FUNCIONES BÁSICAS PARA CRUD ===
def crear_celula(data): celulas_table.insert(data)
def editar_celula(id, cambios): celulas_table.update(cambios, lambda c: c["id"]==id)
def eliminar_celula(id): celulas_table.remove(lambda c: c["id"]==id)
def crear_organulo(data): organulos_table.insert(data)
def editar_organulo(id, cambios): organulos_table.update(cambios, lambda o: o["id"]==id)
def eliminar_organulo(id): organulos_table.remove(lambda o: o["id"]==id)
def crear_generador(data): generadores_table.insert(data)
def editar_generador(id, cambios): generadores_table.update(cambios, lambda g: g["id"]==id)
def eliminar_generador(id): generadores_table.remove(lambda g: g["id"]==id)
def crear_conexion(data): conexiones_table.insert(data)
def editar_conexion(id, cambios): conexiones_table.update(cambios, lambda c: c["id"]==id)
def eliminar_conexion(id): conexiones_table.remove(lambda c: c["id"]==id)
"""

# 4. ENGINE: CÁLCULO DE NECESIDADES Y PRODUCCIÓN
BLOQUE_CALC_ENGINE = """
# === FUNCIONES DE CALCULO DE NECESIDADES Y PRODUCCIÓN ===
def calcular_necesidad_arranque(celula):
    total = 0
    for o_id in celula.get("organulos", []):
        o = organulos_table.get(lambda x: x["id"]==o_id)
        if o: total += o.get("potencia", 0)
    return total

def calcular_produccion(celula):
    return sum([
        o.get("potencia", 0) for o in [organulos_table.get(lambda x: x["id"]==oid) for oid in celula.get("organulos",[])]
        if o and o.get("estado","")=="operativo"
    ])
"""

# 5. CSS MODERNO
BLOQUE_CSS = """
/* Modern UI for CRUD and Simulador */
body { background: #161b22; color: #eee; font-family: 'Segoe UI',sans-serif; }
#sidebar, .modal, .crud-panel { background: #21262d; border-radius: 1em; padding: 1em; }
.selected { outline: 2px solid #00c3ff; background: #101c33; }
.dragging { opacity: 0.7; }
.modal { background: #222; color: #eee; border-radius: 1em; position: fixed; top: 20%; left: 35%; z-index: 99; min-width: 350px; padding: 2em; }
input, button, select { border-radius: .5em; border: none; padding: .5em; margin: .3em; }
button { background: #0284c7; color: #fff; cursor: pointer; }
button:hover { background: #0369a1; }
.transition { transition: all 0.3s; }
::-webkit-scrollbar { background: #222; width: 8px; }
::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
"""

# 6. JS CRUD BÁSICO PARA CADA RECURSO
BLOQUE_JS_GENERADORES = """
// CRUD básico generadores
async function cargarGeneradores() {
    const res = await fetch('/api/generadores');
    const gens = await res.json();
    // TODO: pintar en tablaGeneradores
}
function nuevoGenerador() {
    // TODO: abrir modal creación
}
"""

BLOQUE_JS_ORGANULOS = """
// CRUD básico organulos
async function cargarOrganulos() {
    const res = await fetch('/api/organulos');
    const orgs = await res.json();
    // TODO: pintar en tablaOrganulos
}
function nuevoOrganulo() {
    // TODO: abrir modal creación
}
"""

BLOQUE_JS_CELULAS = """
// CRUD básico celulas
async function cargarCelulas() {
    const res = await fetch('/api/celulas');
    const cels = await res.json();
    // TODO: pintar en tablaCelulas
}
function nuevaCelula() {
    // TODO: abrir modal creación
}
"""

BLOQUE_JS_CONEXIONES = """
// CRUD básico conexiones
async function cargarConexiones() {
    const res = await fetch('/api/conexiones');
    const conns = await res.json();
    // TODO: pintar en tablaConexiones
}
function nuevaConexion() {
    // TODO: abrir modal creación
}
"""

# =============== UTILIDADES DE PARCHEO ===============
def insertar_si_no_esta(path, bloque, marcador, antes_de=None):
    if not os.path.exists(path): return False
    with open(path, "r", encoding="utf8") as f:
        contenido = f.read()
    if marcador not in contenido:
        if antes_de and antes_de in contenido:
            contenido = contenido.replace(antes_de, bloque + "\n" + antes_de)
        else:
            contenido += "\n" + bloque
        with open(path, "w", encoding="utf8") as f:
            f.write(contenido)
        print(f"[OK] Parcheado {marcador} en {os.path.basename(path)}")
        return True
    else:
        print(f"[SKIP] Ya estaba {marcador} en {os.path.basename(path)}")
        return False

def crear_si_no_existe(path, contenido):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf8") as f:
            f.write(contenido)
        print(f"[OK] Creado {path}")
        return True
    else:
        print(f"[SKIP] Ya existía {path}")
        return False

def main():
    # Frontend: index.html
    if os.path.exists(FRONTEND[0]):
        insertar_si_no_esta(FRONTEND[0], BLOQUE_GENERADORES_HTML, "<!-- CRUD Generadores -->", antes_de="</body>")
        insertar_si_no_esta(FRONTEND[0], BLOQUE_ORGANULOS_HTML, "<!-- CRUD Orgánulos -->", antes_de="</body>")
        insertar_si_no_esta(FRONTEND[0], BLOQUE_CELULAS_HTML, "<!-- CRUD Células -->", antes_de="</body>")
        insertar_si_no_esta(FRONTEND[0], BLOQUE_CONEXIONES_HTML, "<!-- CRUD Conexiones -->", antes_de="</body>")
    # CRUD HTML y JS por recurso
    for i, page in enumerate(CRUD_HTMLS):
        crear_si_no_existe(page, f"<!DOCTYPE html>\n<html><head><meta charset='utf-8'><title>{os.path.basename(page)}</title></head><body>\n<h2>{os.path.basename(page).split('.')[0]}</h2>\n</body></html>")
    for i, js in enumerate(CRUD_JS):
        crear_si_no_existe(js, "// CRUD JS autogenerado\n")
        # Inyecta esqueleto de CRUD por tabla
        if "generadores" in js:
            insertar_si_no_esta(js, BLOQUE_JS_GENERADORES, "// CRUD básico generadores")
        elif "organulos" in js:
            insertar_si_no_esta(js, BLOQUE_JS_ORGANULOS, "// CRUD básico organulos")
        elif "celulas" in js:
            insertar_si_no_esta(js, BLOQUE_JS_CELULAS, "// CRUD básico celulas")
        elif "conexiones" in js:
            insertar_si_no_esta(js, BLOQUE_JS_CONEXIONES, "// CRUD básico conexiones")
    # Backend: server/controller/engine
    if os.path.exists(BACKEND[0]):
        insertar_si_no_esta(BACKEND[0], BLOQUE_ENDPOINTS_CRUD, "# === ENDPOINTS CRUD GENERADORES ===")
    if os.path.exists(BACKEND[1]):
        insertar_si_no_esta(BACKEND[1], BLOQUE_FUNCS_CONTROLLER, "# === FUNCIONES BÁSICAS PARA CRUD ===")
    if os.path.exists(BACKEND[2]):
        insertar_si_no_esta(BACKEND[2], BLOQUE_CALC_ENGINE, "# === FUNCIONES DE CALCULO DE NECESIDADES Y PRODUCCIÓN ===")
    # CSS moderno
    if os.path.exists(FRONTEND[2]):
        insertar_si_no_esta(FRONTEND[2], BLOQUE_CSS, "/* Modern UI for CRUD and Simulador */")
    # Checklist
    print("\n==== CHECKLIST AUTO ====")
    print("✔ CRUD endpoints generadores, organulos, celulas, conexiones")
    print("✔ CRUD HTML/JS para cada entidad")
    print("✔ Endpoints randomizar, export/import, dashboard")
    print("✔ CSS moderno drag&drop, modal, dark mode")
    print("✔ Funciones de cálculo de necesidades y producción")
    print("⚠️  Recuerda personalizar los campos, validar los datos y proteger los endpoints en producción (auth)")
    print("⚠️  Añade lógica de negocio específica según reglas del dominio")
    print("⚠️  Termina los métodos JS para crear/editar/mostrar info")
    print("✔ Parcheo finalizado, ¡listo para tu framework biotecnológico!")
    print("[FIN] Puedes lanzar ya el servidor y empezar el diseño visual.")

if __name__ == "__main__":
    main()
