from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from controller import cargar_inicial, evolucionar, impulsar_celula, randomizar_organismo_param, desconectar_celulas
from db import celulas_table, organulos_table, logs_table
import os
from controller import (
    obtener_estado_red, instanciar_celula_tipo, editar_celula,
    eliminar_celula, conectar_celulas, evolucionar, clonar_celula,
    reiniciar_red
)
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Cargar sistema al iniciar
cargar_inicial()

# === ENDPOINTS CRUD UNIVERSAL ===
from db import celulas_table, organulos_table, generadores_table

# --- CELULAS ---
@app.route("/api/celulas", methods=["GET"])
def api_get_celulas():
    return jsonify(celulas_table.all())

@app.route("/api/celulas", methods=["POST"])
def api_post_celula():
    data = request.json
    from controller import crear_celula
    crear_celula(data)
    return jsonify({"ok": True})

@app.route("/api/celulas/<cid>", methods=["GET"])
def api_get_celula(cid):
    celula = celulas_table.get(lambda c: c["id"] == cid)
    return jsonify(celula or {})

@app.route("/api/celulas/<cid>", methods=["PATCH"])
def api_patch_celula(cid):
    cambios = request.json
    from controller import editar_celula
    editar_celula(cid, cambios)
    return jsonify({"ok": True})

@app.route("/api/celulas/<cid>", methods=["DELETE"])
def api_delete_celula(cid):
    from controller import eliminar_celula
    eliminar_celula(cid)
    return jsonify({"ok": True})

# --- ORGANULOS ---
@app.route("/api/organulos", methods=["GET"])
def api_get_organulos():
    return jsonify(organulos_table.all())

@app.route("/api/organulos", methods=["POST"])
def api_post_organulo():
    data = request.json
    from controller import crear_organulo
    crear_organulo(data)
    return jsonify({"ok": True})

@app.route("/api/organulos/<oid>", methods=["GET"])
def api_get_organulo(oid):
    organulo = organulos_table.get(lambda o: o["id"] == oid)
    return jsonify(organulo or {})

@app.route("/api/organulos/<oid>", methods=["PATCH"])
def api_patch_organulo(oid):
    cambios = request.json
    from controller import editar_organulo
    editar_organulo(oid, cambios)
    return jsonify({"ok": True})

@app.route("/api/organulos/<oid>", methods=["DELETE"])
def api_delete_organulo(oid):
    from controller import eliminar_organulo
    eliminar_organulo(oid)
    return jsonify({"ok": True})

# --- GENERADORES ---
@app.route("/api/generadores", methods=["GET"])
def api_get_generadores():
    return jsonify(generadores_table.all())

@app.route("/api/generadores", methods=["POST"])
def api_post_generador():
    data = request.json
    generadores_table.insert(data)
    return jsonify({"ok": True})

@app.route("/api/generadores/<gid>", methods=["GET"])
def api_get_generador(gid):
    gen = generadores_table.get(lambda g: g["id"] == gid)
    return jsonify(gen or {})

@app.route("/api/generadores/<gid>", methods=["PATCH"])
def api_patch_generador(gid):
    cambios = request.json
    generadores_table.update(cambios, lambda g: g["id"] == gid)
    return jsonify({"ok": True})

@app.route("/api/generadores/<gid>", methods=["DELETE"])
def api_delete_generador(gid):
    generadores_table.remove(lambda g: g["id"] == gid)
    return jsonify({"ok": True})

# --- CONEXIONES ---
@app.route("/api/conexiones", methods=["GET"])
def api_get_conexiones():
    # ¡Ajusta según cómo modeles conexiones!
    from controller import obtener_conexiones
    return jsonify(obtener_conexiones())

@app.route("/api/conexiones", methods=["POST"])
def api_post_conexion():
    data = request.json
    from controller import crear_conexion
    crear_conexion(data)
    return jsonify({"ok": True})

@app.route("/api/conexiones/<cid>", methods=["DELETE"])
def api_delete_conexion(cid):
    from controller import eliminar_conexion
    eliminar_conexion(cid)
    return jsonify({"ok": True})

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/app.js')
def app_js():
    return send_from_directory(app.static_folder, 'app.js')

@app.route('/style.css')
def style_css():
    return send_from_directory(app.static_folder, 'style.css')

@app.route('/evolucionar')
def run_evolucion():
    resultado = evolucionar(1)
    return jsonify({"resultado": resultado})

@app.route('/estado')
def estado():
    celulas = celulas_table.all()
    organulos = organulos_table.all()
    return jsonify({"celulas": celulas, "organulos": organulos})

@app.route('/log')
def log():
    logs = logs_table.all()[-20:]
    return jsonify({"logs": logs})

@app.route('/impulsar/<celula_id>')
def impulsar(celula_id):
    ok = impulsar_celula(celula_id)
    if ok:
        return jsonify({"mensaje": f"Célula {celula_id} impulsada correctamente."})
    return jsonify({"error": "Célula no encontrada o sin orgánulo O0."}), 404

@app.route('/sembrar', methods=['POST'])
def sembrar():
    data = request.json
    from db import celulas_table, organulos_table
    from uuid import uuid4

    nueva_id = data.get("id", "CX" + str(uuid4())[:5])
    tipo = data.get("tipo", "G")
    energia = data.get("energia", 1.0)
    x, y = data.get("x", 100), data.get("y", 200)

    organulo_ids = []
    if data.get("solar", False):
        o_id = nueva_id + "-O11"
        organulo_ids.append(o_id)
        organulos_table.insert({"id": o_id, "tipo": "O11", "potencia": 0.1, "estado": "pasivo", "celula_asociada": nueva_id})
    if data.get("manual", False):
        o_id = nueva_id + "-O0"
        organulo_ids.append(o_id)
        organulos_table.insert({"id": o_id, "tipo": "O0", "potencia": 5.0, "estado": "manual", "celula_asociada": nueva_id})

    celulas_table.insert({
        "id": nueva_id,
        "tipo": tipo,
        "energia_actual": energia,
        "energia_maxima": 10,
        "organulos": organulo_ids,
        "estado": "activa",
        "ubicacion": {"x": x, "y": y},
        "nivel_evolucion": 1,
        "enlaces": [],
        "generada_por": None,
        "puede_multiplicar": True,
        "posibles_evoluciones": ["CEA", "CST", "CFB", "CVP"]
    })
    return jsonify({"mensaje": f"Célula {nueva_id} sembrada con éxito."})




# === ENDPOINTS CRUD GENERADORES ===
@app.route("/api/conexiones/<conid>", methods=["PATCH"])
def api_update_conexion(conid):
    from db import conexiones_table
    conexiones_table.update(request.json, lambda c: c["id"] == conid)
    return jsonify({"ok": True})



# === ENDPOINTS RANDOM, EXPORT/IMPORT ===


import logging
logging.basicConfig(filename='server_errors.log', level=logging.ERROR)
@app.errorhandler(Exception)
def handle_exception(e):
    import traceback
    logging.error(traceback.format_exc())
    return jsonify({"ok": False, "error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

